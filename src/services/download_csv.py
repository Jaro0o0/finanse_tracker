import pandas as pd
from pathlib import Path
from models.create_table import engine

desktop = Path.home() / 'Desktop'


def download_csv():
    df = pd.read_sql('SELECT * FROM FINANSE', con=engine)
    file_name = input('Enter file name: ')
    if df.empty:
        print('No expenses found in the database.')
    else:
        output_path = desktop / file_name
        df.to_csv(output_path, index=False)
        print(f'Exported {len(df)} rows to {output_path}')

  


