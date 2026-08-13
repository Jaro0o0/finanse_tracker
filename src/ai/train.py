"""Train the cash-flow model using expenses from the SQLite database."""

import pandas as pd
from neuralprophet import NeuralProphet

from models import cursor


def train_cash_flow(periods: int = 30) -> pd.DataFrame:

  
    cursor.execute('SELECT date, amount FROM FINANSE ORDER BY date')
    rows = cursor.fetchall()
    data = pd.DataFrame(rows, columns=['ds', 'y'])
    data['ds'] = pd.to_datetime(data['ds'])
    data = data.groupby('ds', as_index=False)['y'].sum()

    # if len(data) < 3:
    #     raise ValueError('Do prognozy potrzebne są co najmniej 3 wydatki.')

    model = NeuralProphet(
        yearly_seasonality=False,
        weekly_seasonality=False,
        daily_seasonality=False,
        learning_rate=0.01,
        epochs=100,
        n_lags=7,
       
    )
    model.fit(data, freq='D', progress='none')
    future = model.make_future_dataframe(data, periods=periods, n_historic_predictions=False)
    forecast = model.predict(future)

    print('Prognoza wydatków:')
    print(forecast[['ds', 'yhat1']].to_string(index=False))


if __name__ == '__main__':
    train_cash_flow()
