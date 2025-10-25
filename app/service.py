import pandas as pd
import io, base64, folium, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def analyze_forest_data(data: dict):
    df = pd.DataFrame(data["regions"])

    summary = {
        "region_count": len(df),
        "total_area": df["area"].sum(),
        "avg_altitude": round(df["altitude"].mean(), 2),
        "max_altitude_region": df.loc[df["altitude"].idxmax(), "name"],
        "min_altitude_region": df.loc[df["altitude"].idxmin(), "name"],
    }

    # ✅ matplotlib 그래프
    fig, ax = plt.subplots()
    ax.bar(df["name"], df["area"], color="forestgreen")
    ax.set_title("Forest Area by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Area (ha)")

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    summary["chart"] = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)

    # ✅ folium 지도 (예시용: 임의 좌표)
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=7)  # 기본 서울 중심
    for _, row in df.iterrows():
        # 좌표가 있으면 그걸로, 없으면 랜덤 예시
        lat = 37.5665 + (hash(row["name"]) % 100) / 1000
        lon = 126.9780 + (hash(row["area"]) % 100) / 1000
        popup = f"구역 {row['name']}<br>면적: {row['area']} ha<br>고도: {row['altitude']} m"
        folium.Marker([lat, lon], popup=popup).add_to(m)

    map_html = m._repr_html_()  # HTML 형태로 변환
    summary["map"] = map_html

    return summary
