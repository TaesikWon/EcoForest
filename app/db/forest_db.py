import os, sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "TerraMap.db")  # ✅ 새 DB 이름 반영


def init_forest_db():
    """산림 데이터용 테이블 생성 (없을 경우만)"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS forest_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            area REAL,
            altitude REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_forest_data(region):
    """산림 데이터 1건 저장"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO forest_data (name, area, altitude, date)
        VALUES (?, ?, ?, ?)
    """, (
        region.name,
        region.area,
        region.altitude,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()


def get_all_forest_data():
    """전체 산림 데이터 이력 조회"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM forest_data ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows
