from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from .service import analyze_forest_data
from .model import ForestData
from .db import init_db, save_analysis, get_all_history, get_regions_by_analysis
import io, base64, folium
import matplotlib.pyplot as plt

router = APIRouter()
templates = Jinja2Templates(directory="templates")

init_db()

@router.get("/")
def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@router.post("/analyze")
async def analyze_data(request: Request):
    form = await request.form()
    try:
        regions = [
            {"name": "1", "area": float(form["area1"]), "altitude": float(form["altitude1"])},
            {"name": "2", "area": float(form["area2"]), "altitude": float(form["altitude2"])},
            {"name": "3", "area": float(form["area3"]), "altitude": float(form["altitude3"])},
        ]

        validated = ForestData(regions=regions)
        result = analyze_forest_data(validated.model_dump())
        save_analysis(result)

        return templates.TemplateResponse("result.html", {"request": request, "result": result})

    except ValidationError as ve:
        return templates.TemplateResponse("error.html", {"request": request, "message": f"입력 오류: {ve}"})
    except Exception as e:
        return templates.TemplateResponse("error.html", {"request": request, "message": f"처리 오류: {e}"})


# 🧾 분석 이력 목록 페이지
@router.get("/history")
def show_history(request: Request):
    data = get_all_history()
    return templates.TemplateResponse("history.html", {"request": request, "data": data})


# 🌿 개별 분석 상세 보기 (시각화 포함)
@router.get("/history/{analysis_id}")
def show_history_detail(request: Request, analysis_id: int):
    regions = get_regions_by_analysis(analysis_id)

    # --- matplotlib 시각화 ---
    if regions:
        names = [r[0] for r in regions]
        areas = [r[1] for r in regions]
        fig, ax = plt.subplots()
        ax.bar(names, areas, color="forestgreen")
        ax.set_title("Forest Area by Region")
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        chart = base64.b64encode(buf.read()).decode("utf-8")
        plt.close(fig)
    else:
        chart = None

    # --- folium 지도 시각화 ---
    m = folium.Map(location=[36.5, 127.5], zoom_start=6)
    for i, region in enumerate(regions):
        folium.Marker(
            location=[36.5 + i * 0.2, 127.5 + i * 0.2],
            popup=f"{region[0]} 지역"
        ).add_to(m)
    map_html = m._repr_html_()

    return templates.TemplateResponse(
        "history_detail.html",
        {
            "request": request,
            "regions": regions,
            "chart": chart,
            "map_html": map_html,
        }
    )
