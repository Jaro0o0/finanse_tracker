from models import Expense, cursor, engine
from datetime import date



# CASH_FLOW

# ending nie wpien byc  po dodaniu

def add_finanse():

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

                

            
        


      
