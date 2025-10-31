# routers/geo_router.py

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.models.geo_model import GeoRegion
from app.db.geo_db import init_geo_table, insert_geo_data, fetch_all_geo_data
from app.service import service_ai
import folium, io, base64, matplotlib.pyplot as plt

# ✅ DB 초기화
init_geo_table()

router = APIRouter(prefix="/geo", tags=["geo"])
templates = Jinja2Templates(directory="templates")


# 🚩 도시 분석 입력 폼
@router.get("/analyze")
def show_geo_form(request: Request):
    return templates.TemplateResponse("geo_form.html", {"request": request})


# 🚩 도시 분석 처리
@router.post("/analyze")
async def analyze_geo(request: Request):
    form = await request.form()

    region = GeoRegion(
        city=form["city"],
        population_density=float(form["population_density"]),
        traffic_index=float(form["traffic_index"]),
        green_area=float(form["green_area"]),
    )

    # ✅ AI 입력 데이터
    ai_input = {
        "population_density": region.population_density,
        "traffic_index": region.traffic_index,
        "green_area": region.green_area,
    }
    urban_score = service_ai.predict_ai_score(ai_input, "geo_model")

    # ✅ DB에 점수 포함 저장
    insert_geo_data(region.city, region.population_density, region.traffic_index, region.green_area, urban_score)

    # ✅ 그래프 시각화
    fig, ax = plt.subplots()
    ax.bar([region.city], [region.population_density], color="steelblue")
    ax.set_title(f"{region.city} 인구밀도")
    ax.set_ylabel("명/km²")
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    chart = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)

    # ✅ 지도 시각화
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)
    folium.Marker(
        [37.5665, 126.9780],
        popup=f"{region.city}<br>밀도: {region.population_density:,.1f}",
        icon=folium.Icon(color="blue", icon="building", prefix="fa")
    ).add_to(m)
    map_html = m._repr_html_()

    return templates.TemplateResponse(
        "geo_result.html",
        {
            "request": request,
            "region": region,
            "urban_score": round(urban_score, 2),  # 🔹 AI 예측 점수 표시
            "chart": chart,
            "map_html": map_html,
        }
    )


# 🚩 도시 분석 이력 페이지
@router.get("/history")
def show_geo_history(request: Request):
    data = fetch_all_geo_data()
    return templates.TemplateResponse("geo_history.html", {"request": request, "data": data})
