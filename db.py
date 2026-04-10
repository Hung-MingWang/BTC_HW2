import sqlite3

def init_db():
    conn = sqlite3.connect("data/mnav.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS mnav_data (
        date TEXT PRIMARY KEY,
        mnav REAL,
        ev REAL,
        btc_nav REAL
    )
    """)

    conn.commit()
    conn.close()

def insert_data(date, mnav, ev, btc_nav):
    conn = sqlite3.connect("data/mnav.db")
    c = conn.cursor()

    c.execute("""
    INSERT OR REPLACE INTO mnav_data VALUES (?, ?, ?, ?)
    """, (date, mnav, ev, btc_nav))

    conn.commit()
    conn.close()
