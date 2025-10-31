# service_rag.py
import os
import sqlite3
import logging
from dotenv import load_dotenv
from typing import Optional

# ✅ LangChain + HuggingFace 구성요소
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_chroma import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import ChatPromptTemplate
from transformers import pipeline
from openai import OpenAI

# ----------------------------------------------
# 로깅 설정
# ----------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# ----------------------------------------------
# 환경 변수 로드 (.env / .env.prod 자동 인식)
# ----------------------------------------------
env_file = ".env.prod" if os.getenv("ENV") == "production" else ".env"
load_dotenv(dotenv_path=env_file)

CHROMA_PATH = "./chroma_store"
os.makedirs(CHROMA_PATH, exist_ok=True)

# ----------------------------------------------
# API 키 설정
# ----------------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

# ----------------------------------------------
# 임베딩 모델
# ----------------------------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name=os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
)

# ----------------------------------------------
# SQLite → LangChain 문서 변환
# ----------------------------------------------
def load_eco_geo_docs():
    docs = []
    conn = sqlite3.connect("TerraMap.db")
    cur = conn.cursor()
    try:
        cur.execute("SELECT region, forest_area, air_quality, biodiversity, eco_score FROM eco_data")
        for row in cur.fetchall():
            docs.append(Document(
                page_content=f"지역 {row[0]}의 산림면적은 {row[1]}, 대기질은 {row[2]}, 생물다양성은 {row[3]}, 생태점수는 {row[4]}입니다.",
                metadata={"type": "eco"}
            ))

        cur.execute("SELECT city, population_density, traffic_index, green_area, urban_score FROM geo_data")
        for row in cur.fetchall():
            docs.append(Document(
                page_content=f"도시 {row[0]}의 인구밀도는 {row[1]}, 교통지수는 {row[2]}, 녹지율은 {row[3]}, 도시성장도는 {row[4]}입니다.",
                metadata={"type": "geo"}
            ))

        logger.info(f"✅ {len(docs)}개의 문서 로드 완료")
    except sqlite3.Error as e:
        logger.error(f"⚠️ SQLite 오류: {e}")
    finally:
        conn.close()
    return docs

# ----------------------------------------------
# 벡터스토어 구축
# ----------------------------------------------
def build_vector_store():
    logger.info("🔧 벡터스토어 초기화 중...")
    docs = load_eco_geo_docs()
    if not docs:
        logger.warning("⚠️ 문서 없음 → 중단")
        return None

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)
    vectordb = Chroma.from_documents(split_docs, embedding_model, persist_directory=CHROMA_PATH)
    vectordb.persist()
    logger.info(f"✅ {len(split_docs)}개의 문서가 벡터화되어 저장됨")
    return vectordb

# 최초 실행 시 자동 생성
if not os.path.isfile(os.path.join(CHROMA_PATH, "chroma.sqlite3")):
    build_vector_store()

# ----------------------------------------------
# LLM 초기화 (CPU용)
# ----------------------------------------------
try:
    hf_pipeline = pipeline(
        "text-generation",
        model=os.getenv("GENERATION_MODEL", "mistralai/Mistral-7B-Instruct-v0.2"),
        max_new_tokens=256,
        temperature=0.3,
        device_map=None
    )
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    logger.info("✅ Hugging Face LLM 초기화 완료")
except Exception as e:
    logger.error(f"❌ LLM 초기화 실패: {e}")
    llm = None

# ----------------------------------------------
# RAG 체인 구성
# ----------------------------------------------
try:
    chroma_db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_model)
    retriever = chroma_db.as_retriever()

    prompt = ChatPromptTemplate.from_template("""
    다음은 사용자의 질문과 관련된 문서들입니다:
    {context}

    사용자의 질문: {input}
    문서 내용을 바탕으로 사실에 근거해 자연스럽게 답변하세요.
    """)

    doc_chain = create_stuff_documents_chain(llm, prompt)
    qa_chain = create_retrieval_chain(retriever, doc_chain)
    logger.info("✅ RAG 체인 구성 완료")
except Exception as e:
    logger.error(f"❌ RAG 초기화 실패: {e}")
    qa_chain = None

# ----------------------------------------------
# OpenAI 문체 보정
# ----------------------------------------------
def refine_with_openai(text: str) -> str:
    if not openai_client:
        return text
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "너는 자연스럽고 매끄럽게 문장을 다듬는 편집자야."},
                {"role": "user", "content": f"다음 문장을 자연스럽게 다듬어줘:\n\n{text}"}
            ],
            temperature=0.5,
            max_tokens=512
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"⚠️ OpenAI 보정 오류: {e}")
        return text

# ----------------------------------------------
# 최종 질의 함수
# ----------------------------------------------
def ask_with_rag(query: str) -> str:
    logger.info(f"🔎 [RAG] 질의 수신: {query}")
    if qa_chain is None:
        return "⚠️ RAG 시스템이 초기화되지 않았습니다."
    try:
        result = qa_chain.invoke({"input": query})
        answer = result.get("answer") or result.get("output") or str(result)
        refined = refine_with_openai(answer)
        logger.info("✅ 응답 및 문체 보정 완료")
        return refined
    except Exception as e:
        logger.error(f"⚠️ 질의 오류: {e}")
        return "⚠️ 질의 중 문제가 발생했습니다."
