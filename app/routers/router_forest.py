# app/routers/router_forest.py
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.models.model_forest import ForestRegion
from app.db.forest_db import save_forest_data, get_all_forest_data
from app import service
import io, base64, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# 🚩 산림 분석 입력 폼 페이지
@router.get("/analyze/forest")
def show_forest_form(request: Request):
    return templates.TemplateResponse(
        "forest_form.html",
        {"request": request}
    )


# 🚩 산림 분석 처리
@router.post("/analyze/forest")
async def analyze_forest(
    request: Request,
    name: str = Form(...),
    area: float = Form(...),
    altitude: float = Form(...)
):
    region = ForestRegion(name=name, area=area, altitude=altitude)

    # DB 저장
    save_forest_data(region)

    # 📊 분석 처리 (service.py 사용)
    data = {
        "regions": [
            {"name": region.name, "area": region.area, "altitude": region.altitude}
        ]
    }
    summary = service.analyze_forest_data(data)

    return templates.TemplateResponse(
        "forest_result.html",
        {
            "request": request,
            "region": region,
            "summary": summary,
            "chart": summary["chart"],
            "map_html": summary["map"]
        }
    )


# 🚩 산림 분석 이력 페이지
@router.get("/forest/history")
def show_forest_history(request: Request):
    data = get_all_forest_data()
    return templates.TemplateResponse(
        "forest_history.html",
        {"request": request, "data": data}
    )
