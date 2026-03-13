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

def add_users(telegram_id: int, username: str):
    cursor.execute(
        "INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)",
        (telegram_id, username)
    )
    conn.commit()

#cursor.execute("SELECT * FROM users")
#print(cursor.fetchall())

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id  INTEGER,
    tasks TEXT
    )
""")
conn.commit()

#cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#print(cursor.fetchall())