from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.models.model_geo import GeoRegion
from app.db.geo_db import init_geo_db, save_geo_data, get_all_geo_data
import folium
import io, base64
import matplotlib.pyplot as plt

router = APIRouter()
templates = Jinja2Templates(directory="templates")

init_geo_db()

# 도시 분석
@router.get("/analyze/urban")
def show_urban_form(request: Request):
    return templates.TemplateResponse(request, "geo_form.html", {"request": request})

@router.post("/analyze/urban")
async def analyze_urban(request: Request):
    form = await request.form()

    region = GeoRegion(
        name=form["name"],
        latitude=float(form["latitude"]),
        longitude=float(form["longitude"]),
        population=int(form["population"]),
        population_density=float(form["population_density"]),
        category="urban"
    )

    save_geo_data(region)

    # 그래프 (인구수)
    fig, ax = plt.subplots()
    ax.bar([region.name], [region.population], color="blue")
    ax.set_title(f"{region.name} 인구수")
    ax.set_ylabel("인구 (명)")
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    chart = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)

    # 지도
    m = folium.Map(
        location=[region.latitude, region.longitude],
        zoom_start=13,
        tiles="OpenStreetMap"
    )
    folium.Marker(
        [region.latitude, region.longitude],
        popup=f"{region.name}<br>인구: {region.population:,}명",
        icon=folium.Icon(color="blue", icon="users", prefix="fa")
    ).add_to(m)
    map_html = m._repr_html_()

    return templates.TemplateResponse(
        request, "geo_result.html",
        {"request": request, "region": region, "chart": chart, "map_html": map_html}
    )


# 이력
@router.get("/geo/history")
def show_geo_history(request: Request):
    data = get_all_geo_data()
    return templates.TemplateResponse(request, "geo_history.html", {"request": request, "data": data})