import os, sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "TerraMap.db")


def init_geo_db():
    """🏙️ 도시(지리) 데이터 테이블 생성 (없을 경우만)"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS geo_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            lat REAL,
            lon REAL,
            category TEXT,
            population INTEGER,
            population_density REAL,
            urban_score REAL,      -- ✅ AI 예측 점수 추가
            date TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_geo_data(region, urban_score: float = None):
    """🏙️ 도시 데이터 1건 저장 (+ AI 점수 포함)"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO geo_data (name, lat, lon, category, population, population_density, urban_score, date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        region.name,
        region.latitude,
        region.longitude,
        region.category,
        region.population,
        region.population_density,
        urban_score,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()


def get_all_geo_data():
    """🏙️ 전체 도시 데이터 이력 조회"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM geo_data ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows
