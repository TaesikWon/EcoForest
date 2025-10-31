# app/db/geo_db.py
import sqlite3

DB_PATH = "TerraMap.db"

def init_geo_table():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS geo_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            population_density REAL,
            traffic_index REAL,
            green_area REAL,
            urban_score REAL,  -- ✅ 새 컬럼 추가
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def insert_geo_data(city, population_density, traffic_index, green_area, urban_score):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO geo_data (city, population_density, traffic_index, green_area, urban_score)
        VALUES (?, ?, ?, ?, ?)
    """, (city, population_density, traffic_index, green_area, urban_score))
    conn.commit()
    conn.close()


def fetch_all_geo_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, city, population_density, traffic_index, green_area, urban_score, created_at FROM geo_data")
    rows = cur.fetchall()
    conn.close()
    return rows
