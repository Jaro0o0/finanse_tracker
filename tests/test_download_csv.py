import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))

from services import download_csv as download_module


def test_download_csv_exports_database_to_csv(tmp_path, monkeypatch):
    conn = sqlite3.connect(':memory:')
    conn.execute(
        """
        CREATE TABLE FINANSE (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
        """
    )
    conn.execute(
        "INSERT INTO FINANSE (date, amount, category, description) VALUES (?, ?, ?, ?)",
        ('2026-08-15', 42.5, 'Food', 'Lunch'),
    )
    conn.commit()

    monkeypatch.setattr(download_module, 'engine', conn)
    monkeypatch.setattr(download_module, 'desktop', tmp_path)
    monkeypatch.setattr('builtins.input', lambda _: 'expenses.csv')

    download_module.download_csv()

    csv_path = tmp_path / 'expenses.csv'
    assert csv_path.exists()
    assert 'date,amount,category,description' in csv_path.read_text()
