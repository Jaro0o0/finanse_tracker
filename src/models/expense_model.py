from dataclasses import dataclass
from datetime import date

@dataclass
class Expense:
    amount: float
    date: date
    category: str
    description: str | None = None
