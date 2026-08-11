from models import Expense, cursor, engine
import sys
from datetime import date
import pandas as pd

from pathlib import Path

import subprocess

# CASH_FLOW

# ending nie wpien byc  po dodaniu

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

                cursor.execute(
                    'INSERT INTO FINANSE (date, amount, category, description) VALUES (?, ?, ?, ?)',
                    (
                        user_expnese.date.isoformat(),
                        user_expnese.amount,
                        user_expnese.category,
                        user_expnese.description,
                    ),
                )
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


                        # SHOW_EXPENSES
                        for expenese in expenses:
                            print(f'Amount: {expenese[0]}, Date: {expenese[1]}, Category: {expenese[2]}, Description: {expenese[3]}')


                        #PAth 
                        desktop = Path.home() / "Desktop" / "plik.csv"
                        # TO CSV
                        df = pd.DataFrame(expenses, columns=[desc[0] for desc in cursor.description])
                        df.to_csv( desktop / f'expenses_{year}_{month}.csv', index=False)

            # AI
            case '3':
                cursor.execute('SELECT * FROM FINANSE')
                expenese = cursor.fetchall()


                #Launch Prognose
                if subprocess.poll() is None:
                    print('wait tranning is in progress...')
                else:
                    if len(expenese) >= 3:
                        

                    else:
                        print('Do prognozy potrzebne są co najmniej 3 wydatki.')
                  
                            

                            
                        

      
                   
                        
                    
            case '4':
                sys.exit()
            case _:
                continue
