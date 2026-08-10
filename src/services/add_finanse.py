from models import expense_model
from dataclasses import asdict
import pandas as pd
import sys
from datetime import date

# SQL
from models import engine
from models import cursor



# CASH_FLOW

def add_finanse():
    while True:
        print('1: Add Expense ')
        print('2: View expenses ')
        print('3: Exit  ')

        user_choose = input('Select option').strip()

        match(user_choose):
            case '1':
                amount = round(float(input('enter amount: ')), 4)
                expense_date = date.today()
                cat = input('set categorie: ')
                desc = input('set description: ')

                user_expnese = expense_model(amount, expense_date, cat, desc)

                expnese_df = pd.DataFrame([asdict(user_expnese)])
                expnese_df.to_sql('Finanse', con=engine, if_exists='append', index=False)

                break

                
            case '2':
                print('1: View all expneses')
                print('2: View expneses by mounth')

                view_choose = input('Choose option').strip()

                match(view_choose):
                    case '1':
                        cursor.execute('SELECT * FROME FINANSE')
                        expenses = cursor.fetchall()

                        for expenese in expenses:
                            print(f'Amount: {expenese[0]}, Date: {expenese[1]}, Category: {expenese[2]}, Description: {expenese[3]}')
                    # Mounth_expenses
                    case '2':
                        month = input('select month')
                        year = input('select year')
                        cursor.execute('SELECT * FROME FINANSE WHERE MONTH(date) = ? AND YEAR(date) = ?', (month, year))
                        expenses = cursor.fetchall()

                        for expenese in expenses:
                            print(f'Amount: {expenese[0]}, Date: {expenese[1]}, Category: {expenese[2]}, Description: {expenese[3]}')

            case '3':
                sys.exit()
            case _:
                continue

        if __name__ == "__main__":
            add_finanse()

                

    
        