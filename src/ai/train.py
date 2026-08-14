"""Train the cash-flow model using expenses from the SQLite database."""

import pandas as pd
from neuralprophet import NeuralProphet

from models import cursor


def train_cash_flow(periods: int = 30) -> pd.DataFrame:
    try:
        cursor.execute('SELECT date, amount FROM FINANSE ORDER BY date')
        rows = cursor.fetchall()
        data = pd.DataFrame(rows, columns=['ds', 'y'])
        data['ds'] = pd.to_datetime(data['ds'])
        data = data.groupby('ds', as_index=False)['y'].sum()
        data = data.set_index('ds').asfreq('D', fill_value=0).reset_index()

        if len(data) < 3:
            raise ValueError('Za mało danych do utworzenia prognozy.')

        model = NeuralProphet(
            yearly_seasonality=False,
            weekly_seasonality=False,
            daily_seasonality=False,
            learning_rate=0.01,
            epochs=100,
            n_lags=2,
        
        )
        model.fit(data, freq='D', progress='none')
        future = model.make_future_dataframe(data, periods=periods, n_historic_predictions=False)
        forecast = model.predict(future)
        forecast = forecast[['ds', 'yhat1']].dropna(subset=['yhat1']).copy()
        forecast['yhat1'] = forecast['yhat1'].round(2)
        return forecast
    except Exception:
        print('Nie udało się utworzyć prognozy. Sprawdź, czy masz co najmniej 3 dni wydatków.')
        return pd.DataFrame()


if __name__ == '__main__':
    forecast = train_cash_flow()
    forecast['yhat1'] = forecast['yhat1'].round(2)
    if forecast.empty:
        raise SystemExit(1)


    print('Prognoza wydatków:')
    print(forecast)
