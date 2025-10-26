import os, sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "TerraMap.db")


def init_eco_db():
    """🌿 생태(산림) 데이터 테이블 생성 (없을 경우만)"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS eco_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            area REAL,
            altitude REAL,
            eco_score REAL,        -- ✅ AI 예측 점수 추가
            date TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_eco_data(region, eco_score: float = None):
    """🌿 생태 데이터 1건 저장 (+ AI 점수 포함)"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO eco_data (name, area, altitude, eco_score, date)
        VALUES (?, ?, ?, ?, ?)
    """, (
        region.name,
        region.area,
        region.altitude,
        eco_score,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()


def get_all_eco_data():
    """🌿 전체 생태 데이터 이력 조회"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM eco_data ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows
