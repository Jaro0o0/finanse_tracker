import pandas as pd
from pathlib import Path
from models.create_table import engine

desktop = Path.home() / 'Desktop'

def download_csv():
    df = pd.read_sql('FINANSE',con=engine)
    file_name = input('Enter file name: ')
    if(df.empty):
        print('No expenses found in the database.')
    else:
        csv_expneses = df.to_csv(f'{desktop}/{file_name}',index=False)
        print(csv_expneses)

   
    

   

