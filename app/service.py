import pandas as pd
import io, base64, folium, matplotlib
from datetime import datetime

# 백엔드 환경용 설정 (GUI 백엔드 방지)
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def analyze_forest_data(data: dict):
    """산림 데이터 분석 및 시각화"""
    df = pd.DataFrame(data.get("regions", []))

    if df.empty:
        raise ValueError("⚠️ 데이터가 비어 있습니다. 'regions' 키에 리스트 형태로 데이터가 있어야 합니다.")

    # ✅ 통계 요약 계산
    summary = {
        "region_count": len(df),
        "total_area": round(df["area"].sum(), 2),
        "avg_altitude": round(df["altitude"].mean(), 2),
        "max_altitude_region": df.loc[df["altitude"].idxmax(), "name"],
        "min_altitude_region": df.loc[df["altitude"].idxmin(), "name"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # ✅ matplotlib 그래프
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(df["name"], df["area"], color="forestgreen")
    ax.set_title("🌲 Forest Area by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Area (ha)")
    ax.tick_params(axis='x', rotation=30)

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png", dpi=120)
    buf.seek(0)
    summary["chart"] = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)

    # ✅ folium 지도
    # 중심 좌표 자동 계산 (없으면 서울)
    lat_mean = df["lat"].mean() if "lat" in df.columns else 37.5665
    lon_mean = df["lon"].mean() if "lon" in df.columns else 126.9780

    m = folium.Map(
        location=[lat_mean, lon_mean],
        zoom_start=7,
        tiles="Stamen Terrain",
        attr="Esri, Maxar, Earthstar Geographics, and the GIS User Community"
    )

    for _, row in df.iterrows():
        lat = row.get("lat", lat_mean)
        lon = row.get("lon", lon_mean)
        popup = f"""
        <b>{row.get('name', 'Unknown')}</b><br>
        면적: {row.get('area', 'N/A')} ha<br>
        고도: {row.get('altitude', 'N/A')} m
        """
        folium.Marker(
            [lat, lon],
            popup=popup,
            icon=folium.Icon(color="green", icon="tree-conifer", prefix="glyphicon")
        ).add_to(m)

    summary["map"] = m._repr_html_()

    return summary
