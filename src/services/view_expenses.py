

import pandas as pd
from models import  cursor, engine
from pathlib import Path



def view_expenses():
    print('1: View all expneses')
    print('2: View expneses by mounth')

    view_choose = input('Choose option').strip()

    match(view_choose):
        case '1':
            cursor.execute('SELECT * FROM FINANSE')
            expenses = cursor.fetchall()

            for expenese in expenses:
                print(f'Amount: {expenese[0]}, Date: {expenese[1]}, Category: {expenese[2]}, Description: {expenese[3]}')
        # Mounth_expenses
        case '2':
            month = input('select month')
            year = input('select year')
            cursor.execute(
                "SELECT * FROM FINANSE WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?",
                (month.zfill(2), year),
            )
            expenses = cursor.fetchall()


            # SHOW_EXPENSES
            for expenese in expenses:
                print(f'Amount: {expenese[0]}, Date: {expenese[1]}, Category: {expenese[2]}, Description: {expenese[3]}')


            #PAth 
            desktop = Path.home() / "Desktop" / "plik.csv"
            # TO CSV
            df = pd.DataFrame(expenses, columns=[desc[0] for desc in cursor.description])
            df.to_csv( desktop / f'expenses_{year}_{month}.csv', index=False)



if __name__ == '__main__':
    view_expenses()