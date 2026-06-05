import sqlite3

conn = sqlite3.connect("cita.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    city TEXT,
    plan TEXT,
    score REAL
)
""")

conn.commit()
conn.close()

print("DB READY")
