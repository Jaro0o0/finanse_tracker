from dataclasses import dataclass
from datetime import datetime

@dataclass
class Expense:
    def __int__(self, amount, expense_date, cat, desc):
        self.amount = amount
        self.date = expense_date
        self.cat = cat
        self.desc = desc
