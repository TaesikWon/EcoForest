✅ TerraMap_Requirements.md

📄 저장 경로: C:\Users\play data\TerraMap\TerraMap_Requirements.md

# 🌍 TerraMap_Requirements.md  
**버전:** v2.1  
**작성일:** 2025-10-25  
**작성자:** Taesik Won  

---

## 1️⃣ 프로젝트 개요
**TerraMap**은 FastAPI 기반의 **공간 데이터 시각화 및 분석 웹서비스**입니다.  
사용자가 입력하거나 업로드한 지역 데이터를 바탕으로  
면적, 고도, 분류(category) 등의 통계 정보를 계산하고,  
결과를 지도(folium)와 차트(matplotlib)로 시각화합니다.

---

## 2️⃣ 프로젝트 목표
| 구분 | 목표 |
|------|------|
| 🎯 핵심 목표 | 지역(산림/도시/부동산 등) 데이터를 시각적으로 분석 |
| ⚙️ 기술 목표 | FastAPI + Folium + SQLite 기반 간단한 분석 플랫폼 |
| 💻 운영 목표 | 가벼운 로컬 서버 환경에서도 실행 가능 |
| 🎨 UI 목표 | Bootstrap을 활용한 반응형 웹 UI |

---

## 3️⃣ 시스템 구성 개요



사용자 ─▶ (웹 브라우저)
│
▼
FastAPI 서버
│
▼
Router / Service
│
▼
Database (SQLite)
│
▼
folium 지도 / matplotlib 차트


---

## 4️⃣ 기능 요구사항

| ID | 구분 | 기능명 | 설명 |
|----|------|--------|------|
| FR-01 | 입력 | 지역 데이터 입력 폼 | `/analyze/forest`, `/analyze/urban`, `/analyze/property` |
| FR-02 | 분석 | `/analyze` 엔드포인트 | 면적, 고도, 값(value) 등 평균·최대·최소 계산 |
| FR-03 | 시각화 | 결과 페이지 | folium 지도와 matplotlib 차트 시각화 |
| FR-04 | 저장 | SQLite 저장 | 분석 결과 및 지역별 데이터 로컬 DB에 저장 |
| FR-05 | 이력 | `/history` 페이지 | 분석 내역 리스트 출력 |
| FR-06 | 조회 | `/history/{id}` | 특정 분석 결과 상세보기 |
| FR-07 | UI | Bootstrap 적용 | 모든 HTML 페이지 UI 일관성 유지 |
| FR-08 | 상태 | `/status` | 서버 상태 확인용 API (“ok”) |

---

## 5️⃣ 비기능 요구사항

| 구분 | 항목 | 요구사항 |
|------|------|-----------|
| 💻 성능 | 응답 속도 | 요청 후 1초 이내 처리 |
| 🔒 보안 | 입력 검증 | 폼 데이터 유효성 확인 |
| ⚙️ 유지보수 | 구조화 | router / model / db / templates 분리 |
| 🌐 확장성 | 모듈화 | forest / geo / property 독립 실행 가능 |
| 🎨 UI | 접근성 | Bootstrap 5 반응형 디자인 적용 |
| 🧩 환경 | 호환성 | Windows, macOS, Linux 지원 |
| 📊 데이터 | 저장 방식 | SQLite 단일 파일(`TerraMap.db`) 유지 |

---

## 6️⃣ 기술 스택

| 분류 | 기술 |
|------|------|
| Framework | FastAPI |
| Language | Python 3.11+ |
| Frontend | HTML + Bootstrap + Jinja2 |
| Data Analysis | Pandas + Matplotlib |
| Map Visualization | Folium |
| Database | SQLite |
| Deploy | 로컬 실행 (Uvicorn 기반) |

---

## 7️⃣ 개발 일정 (단기 6주 계획)

| 단계 | 기간 | 목표 | 주요 작업 |
|------|------|------|-----------|
| 1주차 | 10/24 ~ 10/30 | 서버 구조 구축 | FastAPI + Router 분리 |
| 2주차 | 10/31 ~ 11/6 | HTML 폼 및 결과 페이지 | Bootstrap 폼, result 템플릿 완성 |
| 3주차 | 11/7 ~ 11/13 | Forest/Geo 분석 기능 | 면적, 고도 계산 + 차트/지도 표시 |
| 4주차 | 11/14 ~ 11/20 | DB 저장 기능 | SQLite에 분석 결과 저장 |
| 5주차 | 11/21 ~ 11/27 | 이력 및 상세보기 페이지 | /history, /history/{id} 구현 |
| 6주차 | 11/28 ~ 12/4 | 안정화 및 테스트 | 전체 기능 통합 테스트 완료 |

---

## 8️⃣ 향후 확장 방향
- Folium 지도 인터랙션 강화 (클릭 이벤트 등)
- CSV/GeoJSON 업로드 지원
- 분석 결과 다운로드 (CSV/PNG)
- 대시보드 뷰 추가 (Plotly/Chart.js)

---

## 9️⃣ 버전 관리 및 문서 정책


feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 수정
refactor: 코드 구조 개선


- 문서 관리:


/docs
├─ TerraMap_Requirements.md
├─ README.md

- 주요 변경 사항은 README.md에도 요약 반영

---

## 🔚 결론
**TerraMap**은 간단한 지역 데이터 분석과 지도 시각화를 제공하는  
가벼운 FastAPI 기반 플랫폼입니다.  
SQLite와 Folium만으로도 환경 데이터를 직관적으로 탐색하고  
지리적 통찰을 얻을 수 있는 실용적인 구조를 지향합니다.