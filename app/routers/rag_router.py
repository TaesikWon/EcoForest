# app/routers/rag_router.py
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.service.service_rag import ask_with_rag, build_vector_store


# ---------------------------------------
# FastAPI 라우터 설정
# ---------------------------------------
router = APIRouter(prefix="/rag", tags=["rag"])
templates = Jinja2Templates(directory="templates")


# ---------------------------------------
# ✅ 1️⃣ 질의 입력 폼 (GET)
# ---------------------------------------
@router.get("/ask", response_class=HTMLResponse)
def show_rag_form(request: Request):
    """
    사용자에게 RAG 질의 입력 폼 페이지를 표시합니다.
    """
    return templates.TemplateResponse("rag_form.html", {"request": request})


# ---------------------------------------
# ✅ 2️⃣ 질의 처리 (POST)
# ---------------------------------------
@router.post("/ask", response_class=HTMLResponse)
async def process_rag_query(request: Request, query: str = Form(...)):
    """
    사용자의 질문(query)을 받아서 RAG 기반 답변을 생성합니다.
    """
    answer = ask_with_rag(query)
    return templates.TemplateResponse(
        "rag_result.html",
        {
            "request": request,
            "query": query,
            "answer": answer
        },
    )


# ---------------------------------------
# ✅ 3️⃣ 벡터스토어 재구축 (GET)
# ---------------------------------------
@router.get("/rebuild")
def rebuild_vector_db():
    """
    Chroma 벡터스토어를 SQLite 데이터 기반으로 다시 생성합니다.
    """
    build_vector_store()
    return {"message": "✅ Chroma 벡터스토어가 갱신되었습니다."}
