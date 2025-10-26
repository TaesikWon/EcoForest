from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.models.geo_model import GeoRegion
from app.db.geo_db import init_geo_db, save_geo_data, get_all_geo_data
from app.service import service_ai
import folium, io, base64, matplotlib.pyplot as plt

# ✅ DB 초기화
init_geo_db()

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
        name=form["name"],
        latitude=float(form["latitude"]),
        longitude=float(form["longitude"]),
        population=int(form["population"]),
        population_density=float(form["population_density"]),
        category="urban"
    )

    # ✅ AI 입력 데이터
    ai_input = {
        "population": region.population,
        "population_density": region.population_density,
        "latitude": region.latitude,
        "longitude": region.longitude
    }
    urban_score = service_ai.predict_ai_score(ai_input, "geo_model")

    # ✅ DB에 점수 포함 저장
    save_geo_data(region, urban_score)

    # ✅ 그래프 시각화
    fig, ax = plt.subplots()
    ax.bar([region.name], [region.population], color="steelblue")
    ax.set_title(f"{region.name} 인구수")
    ax.set_ylabel("인구 (명)")
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    chart = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)

    # ✅ 지도 시각화
    m = folium.Map(location=[region.latitude, region.longitude], zoom_start=13)
    folium.Marker(
        [region.latitude, region.longitude],
        popup=f"{region.name}<br>인구: {region.population:,}명",
        icon=folium.Icon(color="blue", icon="users", prefix="fa")
    ).add_to(m)
    map_html = m._repr_html_()

    return templates.TemplateResponse(
        "geo_result.html",
        {
            "request": request,
            "region": region,
            "urban_score": round(urban_score, 2),  # 🔹 AI 성장도 표시
            "chart": chart,
            "map_html": map_html,
        }
    )


# 🚩 도시 분석 이력 페이지
@router.get("/history")
def show_geo_history(request: Request):
    data = get_all_geo_data()
    return templates.TemplateResponse("geo_history.html", {"request": request, "data": data})
