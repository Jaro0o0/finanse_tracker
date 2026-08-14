import time
from rich.progress import track
from models import cursor
import pandas as pd
from ai.run_subprocess import run_forecast


# TENEING Z CSV

def forecast():
    cursor.execute('SELECT * FROM FINANSE')
    expenses = cursor.fetchall()

    if len(expenses) < 3:
        print('Do prognozy potrzebne są co najmniej 3 wydatki.')
        print('If you have a CSV file with expenses, you can import it to the database.')
        user_input = input('Do you want to import expenses from a CSV file? (y/n)').strip().lower()
        match(user_input):
            case 'y':
                csv_location = input('enter csv file location:').strip()
                try:
                    df = pd.read_csv(f'{csv_location}')
                except FileNotFoundError:
                    print(f'file not found chceck your file location {csv_location} ')
                except pd.errors.EmptyDataError:
                    print('CSV file is empty')
    

    
    for i in track(range(100), description='Training model...'):
        time.sleep(0.01)
    output = run_forecast()
    print(output or 'Skrypt treningu nie zwrócił prognozy.')
