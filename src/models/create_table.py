import sqlite3

engine = sqlite3.connect('finanse.db')
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
