

import pandas as pd

from models import  cursor, engine
from pathlib import Path

#STYLE
from rich import print
from rich.table import Table





def view_expenses():
    print('[bold light_steel_blue1]1: View all expenses[/]')
    print('[bold light_steel_blue1]2: View expenses by month[/]')

    view_choose = input('Choose option: ').strip()

    match(view_choose):
        case '1':
            cursor.execute('SELECT * FROM FINANSE')
            expenses = cursor.fetchall()
            #CREATE_TABLE
            table = Table(title='Expenses')
            table.add_column('Amount', justify='right', style='cyan', no_wrap=True)
            table.add_column('Date', style='magenta')
            table.add_column('Category', style='green')
            table.add_column('Description', style='yellow') 

            for expenese in expenses:
                table.add_row(*(str(value) for value in expenese))
            print(table)
        # Mounth_expenses
        case '2':
            month = input('select month: ').strip()
            year = input('select year: ').strip()
            cursor.execute(
                "SELECT * FROM FINANSE WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?",
                (month.zfill(2), year),
            )
            expenses = cursor.fetchall()
            #CREATE_TABLE
            table = Table(title=f'Expenses for {month}/{year}')
            table.add_column('Amount', justify='right', style='cyan', no_wrap=True)
            table.add_column('Date', style='magenta')
            table.add_column('Category', style='green')
            table.add_column('Description', style='yellow')


            # SHOW_EXPENSES
            for expenese in expenses:
                table.add_row(*(str(value) for value in expenese))
            print(table)

            # #PAth 
            # desktop = Path.home() / "Desktop" / "plik.csv"
            # # TO CSV
            # df = pd.DataFrame(expenses, columns=[desc[0] for desc in cursor.description])
            # df.to_csv( desktop / f'expenses_{year}_{month}.csv', index=False)



if __name__ == '__main__':
    view_expenses()
