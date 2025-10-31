# app/db/eco_db.py
import sqlite3

DB_PATH = "TerraMap.db"

def init_eco_table():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS eco_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region TEXT,
            forest_area REAL,
            air_quality REAL,
            biodiversity REAL,
            eco_score REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def insert_eco_data(region, forest_area, air_quality, biodiversity, eco_score):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO eco_data (region, forest_area, air_quality, biodiversity, eco_score)
        VALUES (?, ?, ?, ?, ?)
    """, (region, forest_area, air_quality, biodiversity, eco_score))
    conn.commit()
    conn.close()


def fetch_all_eco_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, region, forest_area, air_quality, biodiversity, eco_score, created_at FROM eco_data")
    rows = cur.fetchall()
    conn.close()
    return rows
