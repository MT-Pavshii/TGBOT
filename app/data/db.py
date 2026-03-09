import sqlite3

conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    username TEXT
    )
""")

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print (row)