# 🗺️ TerraMap

**공간지리 데이터를 통해 산림과 도시를 분석하고 시각화하는 AI 기반 통합 환경 분석 플랫폼**

---

## 🌿 프로젝트의 배경과 목적

자연과 도시의 균형은 지속 가능한 미래를 위한 필수 조건입니다.
그러나 현실은 매년 반복되는 산불, 산사태, 도시 과밀화로 인해
생태계와 지역 사회가 심각한 위협을 받고 있습니다.

이런 문제를 해결하기 위한 시스템들은 대부분 공공기관 중심으로 구축되어
일반 개인이나 지역 커뮤니티가 쉽게 활용하기 어렵습니다.

**TerraMap은 바로 이 한계를 넘어,**

> "누구나 공간지리 데이터를 분석하고,  
> 환경 보전과 도시 계획에 직접 기여할 수 있도록 하자."

는 생각에서 출발했습니다.

이 프로젝트는 기술을 통해
자연과 인간, 개발과 보전이 공존하는 세상을 만들어가는 실험입니다.

---

## 🌍 프로젝트 개요

TerraMap은 FastAPI 기반의 웹 애플리케이션으로,
산림과 도시 데이터를 입력받아
통계적 분석, 지도 시각화, 그리고 AI 기반 의미 해석을 수행합니다.

최신 버전에서는 LangChain과 HuggingFace, OpenAI API를 결합한
RAG(Retrieval-Augmented Generation) 기술을 통해
데이터 기반 질의응답과 자연스러운 보고서 생성을 지원합니다.

---

## ⚙️ 기술 스택

| 구분 | 기술 |
|------|------|
| **Backend** | FastAPI, Uvicorn |
| **AI Engine** | LangChain, HuggingFace (Mistral 7B), OpenAI GPT-4o-mini |
| **Vector DB** | Chroma |
| **Embedding** | Sentence Transformers (all-MiniLM-L6-v2) |
| **Database** | SQLite |
| **Visualization** | Folium, Matplotlib |
| **Environment** | Python 3.11+, dotenv |

---

## 🧠 핵심 기능

### 🌲 생태 데이터 분석

- 산림면적, 대기질, 생물다양성 등 환경 지표 계산
- AI가 데이터 기반 설명문 생성  
  (예: "이 지역은 산림 비율이 높아 생태점수가 우수합니다.")
- Folium 기반 지도 시각화

### 🏙️ 도시 데이터 분석

- 인구밀도, 교통지수, 녹지율 분석
- 도시 성장도 및 환경 영향도 계산
- 시각적 대시보드 + AI 분석 요약

### 🤖 AI RAG 기반 분석

- LangChain + Chroma로 문서 벡터 검색
- **HuggingFace (Mistral-7B)** 로 초안 생성
- OpenAI GPT-4o-mini로 문장 자연스러운 보정

---

## 🧩 아키텍처 개요
```
 ┌────────────────────────────────────────────┐
 │                TerraMap API                │
 │────────────────────────────────────────────│
 │ FastAPI  ·  SQLite  ·  Templates (Jinja2)  │
 └────────────────────────────────────────────┘
                │
                ▼
 ┌────────────────────────────────────────────┐
 │           RAG (Retrieval-Augmented)        │
 │────────────────────────────────────────────│
 │ LangChain + Chroma + HuggingFacePipeline   │
 │ OpenAI GPT-4o-mini 문체 보정                │
 └────────────────────────────────────────────┘
                │
                ▼
 ┌────────────────────────────────────────────┐
 │             사용자 웹 인터페이스            │
 │────────────────────────────────────────────│
 │ Folium 지도 · 분석 차트 · 결과 리포트       │
 └────────────────────────────────────────────┘
```

---

## 📁 프로젝트 구조
```
TerraMap/
├── app/
│   ├── routers/
│   │   ├── eco_router.py
│   │   └── geo_router.py
│   ├── service/
│   │   └── service_rag.py      # ✅ RAG + LLM 핵심 로직
│   ├── models/
│   ├── db/
│   └── main.py                 # FastAPI 실행 진입점
│
├── chroma_store/               # 벡터 데이터 저장소
├── templates/                  # HTML 템플릿
├── requirements.txt
├── .env                        # API 키, 환경변수
└── README.md
```

---

## 🚀 실행 방법

### 1️⃣ 가상환경 생성 및 활성화
```bash
python -m venv .venv
.venv\Scripts\activate   # (Windows)
# source .venv/bin/activate  # (macOS/Linux)
```

### 2️⃣ 패키지 설치
```bash
pip install -r requirements.txt
```

### 3️⃣ 서버 실행
```bash
uvicorn app.main:app --reload
```

### 4️⃣ 브라우저 접속
```
http://localhost:8000
```

---

## 🎯 TerraMap의 기대 효과

| 구분 | 기대 효과 |
|------|-----------|
| 🌱 **환경적 효과** | 누구나 생태·도시 데이터를 직접 분석하고 시각화하여 환경 이해와 보전 의식 향상 |
| 📚 **교육적 효과** | 데이터 과학과 환경 분석을 결합한 학습 플랫폼으로 활용 가능 |
| 💻 **기술적 효과** | FastAPI, LangChain, HuggingFace 등 실무 오픈소스 기술의 통합 예시 |
| 🌍 **사회적 효과** | 공공 데이터 접근성을 높여 개인·지역사회가 환경 데이터를 쉽게 활용할 수 있도록 지원 |

---

## 🧭 향후 로드맵

| 단계 | 목표 | 설명 |
|------|------|------|
| ✅ **1단계** | 환경 데이터 분석 시스템 구축 | FastAPI + SQLite + Folium 시각화 |
| ✅ **2단계** | AI 분석 기능 통합 | HuggingFace + OpenAI 기반 RAG |
| 🔄 **3단계** | 실시간 공공데이터 API 연동 | 산림청·통계청 데이터 자동 갱신 |
| ⏳ **4단계** | Terra-LM 모델 개발 | 환경 분석 특화 미세조정 모델 구축 |
| 🚀 **5단계** | 클라우드 배포 및 대시보드 | Render / Railway 기반 웹 서비스화 |

---

## 👤 개발자

**Taesik Won**

- Backend & AI Developer
- Focus: Generative AI, NLP, RAG Systems
- GitHub: [@TaesikWon](https://github.com/TaesikWon)

---

## 📜 라이선스

본 프로젝트는 학습 및 연구 목적의 오픈소스 예시이며, 무단 상업적 이용 및 재배포를 금합니다.

---

> **"TerraMap은 데이터를 통해 지구를 이해하고,  
> AI로 자연과 도시의 조화를 설계하는 프로젝트입니다."** 🌎