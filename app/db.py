import sqlite3
from datetime import datetime

DB_PATH = "ecoforest.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # ① 분석 결과 테이블
    cur.execute("""
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            total_area REAL,
            avg_altitude REAL,
            max_region TEXT,
            min_region TEXT
        )
    """)

    # ② 새로 추가할 구역별 데이터 테이블
    cur.execute("""
        CREATE TABLE IF NOT EXISTS forest_regions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            analysis_id INTEGER,
            region_name TEXT,
            area REAL,
            altitude REAL,
            FOREIGN KEY (analysis_id) REFERENCES analysis_history (id)
        )
    """)

    conn.commit()
    conn.close()


def save_analysis(result: dict):
    """분석 요약(analysis_history) 저장"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO analysis_history (date, total_area, avg_altitude, max_region, min_region)
        VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        result["total_area"],
        result["avg_altitude"],
        result["max_altitude_region"],
        result["min_altitude_region"],
    ))

    analysis_id = cur.lastrowid  # 방금 저장된 분석 ID

    # forest_regions 데이터가 있으면 함께 저장
    if "regions" in result:
        for region in result["regions"]:
            cur.execute("""
                INSERT INTO forest_regions (analysis_id, region_name, area, altitude)
                VALUES (?, ?, ?, ?)
            """, (
                analysis_id,
                region["name"],
                region["area"],
                region["altitude"],
            ))

    conn.commit()
    conn.close()


def get_all_history():
    """분석 요약 목록 조회"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM analysis_history ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_regions_by_analysis(analysis_id: int):
    """특정 분석 ID에 연결된 구역 데이터 조회"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT region_name, area, altitude FROM forest_regions WHERE analysis_id=?", (analysis_id,))
    rows = cur.fetchall()
    conn.close()
    return rows
