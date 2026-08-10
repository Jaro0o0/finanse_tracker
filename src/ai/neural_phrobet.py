import pandas as pd
from neuralprophet import NeuralProphet

#SQL
from models import engine
from models import cursor



def train_cash_flow(df: pd.DataFrame):
    model = NeuralProphet(
        n_lags=30,
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=True,
    )


    cursor.execute('SELECT date, amount FROM FINANSE')
    data = cursor.fetchall()



    print("Start traning...")
    metrics = model.fit(df, freq="D")