# 🌿 EcoForest

**EcoForest**는 **FastAPI 기반 산림 생태 데이터 분석 웹 서비스**입니다.  
사용자가 직접 데이터를 입력하거나 업로드하면,  
웹에서 바로 산림 면적·고도 등의 분석 결과를 확인할 수 있습니다.  
향후에는 **GeoPandas**를 활용한 공간 데이터 분석 기능으로 확장될 예정입니다.

---

## 🚀 주요 기능

- **FastAPI 백엔드 서버**  
  - `/analyze` 엔드포인트를 통해 JSON 형태의 데이터를 분석  
  - 총 면적(`total_area`)과 평균 고도(`average_altitude`) 계산  

- **HTML 템플릿 렌더링**  
  - 브라우저에서 분석 결과를 시각적으로 확인 가능  
  - `form.html`에서 데이터 입력, `result.html`에서 결과 출력  

- **확장성 높은 구조**  
  - `router.py`, `service.py` 분리로 유지보수 용이  
  - 향후 GeoPandas, AI 모델 분석 모듈 추가 가능  

---

## 📂 폴더 구조

EcoForest/
│
├─ app/
│ ├─ router.py # 라우터 (엔드포인트 관리)
│ ├─ service.py # 분석 로직 처리
│ └─ model.py # (추후 데이터 모델 확장 예정)
│
├─ templates/
│ ├─ base.html
│ ├─ form.html
│ └─ result.html
│
├─ static/ # (정적 파일 경로)
│
├─ main.py # FastAPI 실행 진입점
├─ requirements.txt # 의존성 패키지 목록
└─ README.md

yaml
코드 복사

---

## 🧩 실행 방법

1️⃣ 가상환경(venv) 활성화  
```bash
venv\Scripts\activate
2️⃣ 필요한 패키지 설치

bash
코드 복사
pip install -r requirements.txt
3️⃣ 서버 실행

bash
코드 복사
uvicorn app.main:app --reload
4️⃣ 브라우저 접속
👉 http://127.0.0.1:8000

🌲 향후 계획
GeoPandas 기반 공간 데이터 분석 기능 추가

산림 변화 추적 및 시각화 기능 구현

데이터베이스 연동 (PostgreSQL + PostGIS)

REST API 확장 (외부 시스템과 연동)

🧠 개발 정보
프로젝트명: EcoForest

개발자: Taesik Won

프레임워크: FastAPI

언어: Python 3.10+

라이선스: MIT License

📘 EcoForest는 단순한 분석 도구가 아니라,
“숲의 데이터를 통해 생태를 이해하는 AI 기반 플랫폼”을 목표로 합니다.