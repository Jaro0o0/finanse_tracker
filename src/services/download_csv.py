import pandas as pd


def download_csv():
    df = pd.read_sql('FINANSE',con=engine)
    file_name = input('Enter file name: ')
    csv_expneses = df.to_csv(f'{file_name}',index=False)
    print(csv_expneses)
    