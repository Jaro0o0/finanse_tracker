from models import Expense, cursor, engine
from dataclasses import asdict
import pandas as pd
import sys
from datetime import date
import subprocess

# CASH_FLOW



def add_finanse():
    while True:
        print('1: Add Expense ')
        print('2: View expenses ')
        print('3: AI expenses prognose ')
        print('4: Exit  ')

        user_choose = input('Select option').strip()

        match(user_choose):
            case '1':
                amount = round(float(input('enter amount: ')), 4)
                expense_date = date.today()
                cat = input('set categorie: ')
                desc = input('set description: ')

                user_expnese = Expense(amount, expense_date, cat, desc)

                expnese_df = pd.DataFrame([asdict(user_expnese)])
                expnese_df.to_sql('Finanse', con=engine, if_exists='append', index=False)
                engine.commit()

                break

                
            case '2':
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

                        for expenese in expenses:
                            print(f'Amount: {expenese[0]}, Date: {expenese[1]}, Category: {expenese[2]}, Description: {expenese[3]}')

            case '3':
                cursor.execute('SELECT * FROM FINANSE')
                expenese = cursor.fetchall()

                if len(expenese) >= 3:
                    print('Prognoza AI nie jest jeszcze podłączona do menu.')
                    p = subprocess.Popen(
                        ['python', 'src/ai/train.py'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        text=True
                        )
                else:
                    print('AI model have to have minimum 3 expenses data ')
                    
            case '4':
                sys.exit()
            case _:
                continue
