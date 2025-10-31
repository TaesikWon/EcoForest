# routers/eco_router.py

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.models.eco_model import EcoRegion
from app.db.eco_db import init_eco_table, insert_eco_data, fetch_all_eco_data
from app import service
from app.service import service_ai

# ✅ DB 초기화
init_eco_table()

router = APIRouter(prefix="/eco", tags=["eco"])
templates = Jinja2Templates(directory="templates")


# 🚩 생태 분석 입력 폼
@router.get("/analyze")
def show_eco_form(request: Request):
    return templates.TemplateResponse("eco_form.html", {"request": request})


# 🚩 생태 분석 처리
@router.post("/analyze")
async def analyze_eco(
    request: Request,
    name: str = Form(...),
    forest_area: float = Form(...),
    air_quality: float = Form(...),
    biodiversity: float = Form(...),
):
    # ✅ 입력값 모델화
    region = EcoRegion(name=name, forest_area=forest_area, air_quality=air_quality, biodiversity=biodiversity)

    # ✅ AI 입력 데이터 구성
    ai_input = {
        "forest_area": region.forest_area,
        "air_quality": region.air_quality,
        "biodiversity": region.biodiversity,
    }
    eco_score = service_ai.predict_ai_score(ai_input, "eco_model")

    # ✅ 데이터 + 점수 함께 저장
    insert_eco_data(region.name, region.forest_area, region.air_quality, region.biodiversity, eco_score)

    # ✅ 기존 통계 분석
    data = {"regions": [{"name": region.name, "forest_area": region.forest_area}]}
    summary = service.analyze_forest_data(data)

    return templates.TemplateResponse(
        "eco_result.html",
        {
            "request": request,
            "region": region,
            "summary": summary,
            "eco_score": round(eco_score, 2),  # 🔹 AI 예측 점수 표시
            "chart": summary["chart"],
            "map_html": summary["map"],
        },
    )


# 🚩 생태 분석 이력 페이지
@router.get("/history")
def show_eco_history(request: Request):
    data = fetch_all_eco_data()
    return templates.TemplateResponse("eco_history.html", {"request": request, "data": data})
