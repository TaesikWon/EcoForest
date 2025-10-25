import os, sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "TerraMap.db")

def init_geo_db():
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
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_geo_data(region):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO geo_data (name, lat, lon, category, population, population_density, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        region.name,
        region.latitude,
        region.longitude,
        region.category,
        region.population,
        region.population_density,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()

def get_all_geo_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM geo_data ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows