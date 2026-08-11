import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).with_name('finanse.db')
engine = sqlite3.connect(DATABASE_PATH)
cursor = engine.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS FINANSE (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT
) ''')


engine.commit()
