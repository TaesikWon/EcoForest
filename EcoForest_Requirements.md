🌲 EcoForest_Requirements.md

버전: v1.1
작성일: 2025-10-24
작성자: Taesik Won


1️⃣ 프로젝트 개요
EcoForest는 FastAPI 기반의 산림 생태 데이터 분석 웹서비스입니다.
사용자가 입력하거나 업로드한 산림 데이터를 분석하여
면적, 고도, 토양, 기상 요인 등을 기반으로
산림 상태를 진단하고,
향후에는 AI 기반 재해 예측 서비스로 확장될 예정입니다.


2️⃣ 프로젝트 목표
🎯 핵심 목표	산림 데이터를 활용한 환경 분석 및 재해 예측 플랫폼 구축
🌐 기술 목표	FastAPI + GeoPandas + PostgreSQL(PostGIS)을 활용한 분석 서비스 구현
🧠 AI 목표	RAG 기반 모델을 적용해 사용자 질의응답형 분석 기능 제공
🌱 사회적 목표	공공 데이터 활용을 통한 산림 재해 예방 및 생태 이해 증진


3️⃣ 시스템 구성 개요
🔸 구성도 (개념적)
사용자 ─▶ (웹 브라우저)
           │
           ▼
     FastAPI 서버
           │
           ▼
     Service (분석 로직)
           │
           ▼
     Database (PostgreSQL + PostGIS)
           │
           ▼
     AI 모듈 (RAG / LLM, 향후 확장)

4️⃣ 기능 요구사항
ID	구분	기능명	설명
FR-01	입력	사용자 입력 폼	웹 폼(form.html)에서 면적, 고도 등 산림 데이터 입력
FR-02	분석	/analyze 엔드포인트	JSON 데이터 분석 — 총 면적, 평균 고도 계산
FR-03	출력	result.html	분석 결과를 시각적으로 표시
FR-04	상태	/status 엔드포인트	서버 상태 “ok” 응답
FR-05	데이터베이스 (예정)	PostgreSQL 연동	분석 결과 저장 및 이력 관리
FR-06	공간 분석 (예정)	GeoPandas 적용	GeoJSON/Shapefile 기반 공간 데이터 처리
FR-07	AI 분석 (예정)	RAG 모듈	산사태, 산불 등 재해 예측 모델 적용
FR-08	알림 (예정)	사용자 알림	위험 지역 감지 시 사용자 알림 기능


5️⃣ 비기능 요구사항
구분	항목	요구사항
💻 성능	응답 속도	요청 후 1초 이내 응답
🔒 보안	데이터 검증	JSON 입력 데이터 형식 유효성 검사
⚙️ 유지보수	구조화	router, service, model 모듈화 유지
🌐 확장성	모듈 구조	AI/GeoPandas/DB 기능 독립적 확장 가능
🎨 UI	접근성	브라우저 기반 시각화, 모바일 대응 예정
🧩 환경	호환성	Windows / macOS / Linux 지원
📊 로그	기록 관리	요청, 분석 결과 로그 저장 (예정)


6️⃣ 기술 스택
분류	기술
Framework	FastAPI
Language	Python 3.10+
Frontend	HTML, Jinja2 Template
Data Analysis	Pandas, GeoPandas (예정)
Database	PostgreSQL + PostGIS (예정)
AI / NLP	LangChain, OpenAI API (예정)
Deploy	Render / Railway / Docker (예정)


7️⃣ 개발 일정 (6주 단기 스프린트)
단계	기간 (예상)	주요 목표	세부 내용
1주차	10/24 ~ 10/30	FastAPI 서버 구축	서버 실행, /analyze /status 구현, router/service 구조 완성
2주차	10/31 ~ 11/6	HTML 템플릿 연결	form.html, result.html 연결 및 결과 표시
3주차	11/7 ~ 11/13	GeoPandas 분석 추가	GeoJSON 기반 공간 데이터 처리 기능 구현
4주차	11/14 ~ 11/20	PostgreSQL + PostGIS 연동	분석 결과 DB 저장 및 쿼리 기능 추가
5주차	11/21 ~ 11/27	RAG 기반 AI 분석 기능	LangChain + OpenAI 연동 테스트
6주차	11/28 ~ 12/4	통합 테스트 및 배포	전체 기능 테스트 및 Render/Railway 배포


8️⃣ 향후 확장 방향
- GeoPandas 기반 지형·공간 데이터 분석 고도화
- AI 기반 산림 재해 예측 모델 (RAG, GPT, ML)
- 지도 시각화 서비스 (folium / leaflet / maplibre)
- 사용자 맞춤형 대시보드 및 알림 서비스


9️⃣ 버전 관리 및 문서 정책
모든 변경 사항은 Git 커밋 컨벤션 준수

feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 수정
refactor: 코드 구조 개선
문서는 /docs 폴더에 정리 (예정)
README.md → 프로젝트 소개용
EcoForest_Requirements.md → 기술/요구사항 명세용


🔚 결론
EcoForest는 데이터 과학과 AI를 결합해
산림 재해를 예측하고 환경 데이터를 통해
공공 가치 창출을 목표로 하는 실무형 프로젝트입니다.