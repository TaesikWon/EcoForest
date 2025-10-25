🌲 EcoForest 🌲

🌿 프로젝트의 동기와 의도

1️⃣ 산림 재해에 대한 문제의식

매년 반복되는 산사태, 산불, 홍수 등 산림 기반 재해는 인명·재산 피해를 초래합니다.

대부분의 예측 시스템은 대규모 기관 중심이며,
개인이나 소규모 단체가 쉽게 활용할 수 있는 분석 도구는 부족합니다.

EcoForest는 이러한 문제를 해결하기 위해,
산림 데이터를 기반으로 재해 발생 가능성을 분석·시각화하는 웹서비스를 목표로 합니다.


2️⃣ 데이터 과학과 공공의 연결

단순한 기술 시연이 아니라,
데이터 분석과 AI 기술을 실제 환경·공공 문제 해결에 적용하는 것을 목표로 합니다.

기상청, 국토정보공사 등 공공데이터를 활용해
지형, 토양, 강우 등의 요인을 분석하고,
재해 위험 지역을 식별 및 예측하는 모델로 확장할 예정입니다.


3️⃣ 개인 기술 성장의 목적

FastAPI, GeoPandas, PostgreSQL, 
RAG, AI 분석 등
실무 수준의 기술 스택을 통합해보며
실제 서비스 수준의 프로젝트를 구현하는 것을 목표로 합니다.
결과물은 포트폴리오 및 실무 데모용으로도 활용 가능합니다.


4️⃣ 서비스로의 발전 방향

초기 단계에서는 산림 데이터 분석 및 시각화를 중심으로 시작하지만,
장기적으로는 지능형 산림 재해 예측 플랫폼으로 확장할 계획입니다.

🌦️ 실시간 위험 감지 (강우·지형 데이터 통합)
🗺️ 지도 기반 시각화 (folium / leaflet / maplibre)
🤖 AI 기반 질의응답 (RAG)
🔔 사용자 맞춤형 알림 서비스 (재해 발생 예측 시)


📘 프로젝트 개요

EcoForest는 FastAPI 기반 산림 생태 데이터 분석 웹 서비스입니다.
사용자가 직접 데이터를 입력하거나 업로드하면,
웹에서 바로 산림 면적·고도 등의 분석 결과를 확인할 수 있습니다.
향후에는 GeoPandas를 활용한 공간 데이터 분석 기능과
AI 기반 재해 예측 모델로 확장될 예정입니다.


🚀 주요 기능 🚀

🧠 FastAPI 백엔드 서버
/analyze 엔드포인트를 통해 JSON 형태의 데이터를 분석

총 면적(total_area)과 평균 고도(average_altitude) 계산


🖥️ HTML 템플릿 렌더링
브라우저에서 분석 결과를 시각적으로 확인 가능

form.html에서 데이터 입력, result.html에서 결과 출력.


🧩 확장성 높은 구조

router.py, service.py 분리로 유지보수 용이

향후 GeoPandas, AI 모델, RAG 기반 질의응답 모듈 추가 가능.


📂 폴더 구조

EcoForest/
├─ app/
│   ├─ router.py        # 라우터 (엔드포인트 관리)
│   ├─ service.py       # 분석 로직 처리
│   └─ model.py         # (추후 데이터 모델 확장 예정)
│
├─ templates/
│   ├─ base.html
│   ├─ form.html
│   └─ result.html
│
├─ static/              # (정적 파일 경로)
├─ main.py              # FastAPI 실행 진입점
├─ requirements.txt     # 의존성 패키지 목록
└─ README.md


🧰 기술 스택

분야	기술
백엔드	FastAPI, Uvicorn
데이터 분석	Pandas, (예정) GeoPandas, Shapely
AI / RAG	OpenAI API, LangChain (예정)
DB / GIS	PostgreSQL, PostGIS (예정)
프론트엔드	Jinja2 (템플릿), HTML/CSS
배포	(예정) Render / Railway / Docker


🧪 사용 예시
요청 예시 (POST /analyze)
[
  {"area": 120, "altitude": 300},
  {"area": 90, "altitude": 280},
  {"area": 150, "altitude": 350}
]

응답 예시
{
  "total_area": 360,
  "average_altitude": 310.0,
  "message": "산림 데이터 분석 완료 ✅"
}


⚙️ 실행 방법

1️⃣ 가상환경(venv) 활성화
venv\Scripts\activate


2️⃣ 필요한 패키지 설치
pip install -r requirements.txt


3️⃣ 서버 실행
uvicorn app.main:app --reload


4️⃣ 브라우저 접속
👉 http://127.0.0.1:8000


⚙️ 이 주소는 로컬 테스트용이며, 배포 시 실제 URL로 변경 예정입니다.


🌲 향후 계획

GeoPandas 기반 공간 데이터 분석 기능 추가.
산림 변화 추적 및 시각화 기능 구현.
PostgreSQL + PostGIS 연동.
REST API 확장 (외부 시스템 연계)
RAG(AI 기반 질의응답) 기능 도입.


🧠 개발 정보
항목	내용
프로젝트명	EcoForest
개발자	Taesik Won
프레임워크	FastAPI
언어	Python 3.10+
라이선스	MIT License


📘 EcoForest는 단순한 분석 도구가 아니라,
**“숲의 데이터를 통해 생태를 이해하고 재해를 예측하는 AI 기반 플랫폼”**을 목표로 합니다.