# app/db.py
import sqlite3
from datetime import datetime

DB_PATH = "ecoforest.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
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
    conn.commit()
    conn.close()

def save_analysis(result: dict):
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
    conn.commit()
    conn.close()

def get_all_history():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM analysis_history ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows
