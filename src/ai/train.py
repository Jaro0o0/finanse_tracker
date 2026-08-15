
import pandas as pd
from neuralprophet import NeuralProphet
from rich.console import Console
from rich.table import Table

from models import cursor


def train_cash_flow(periods: int = 30) -> pd.DataFrame:
    try:
        cursor.execute('SELECT date, amount FROM FINANSE ORDER BY date')
        rows = cursor.fetchall()
        data = pd.DataFrame(rows, columns=['ds', 'y'])
        data['ds'] = pd.to_datetime(data['ds'])
        data = data.groupby('ds', as_index=False)['y'].sum()
        data = data.set_index('ds').asfreq('D', fill_value=0).reset_index()

        

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
        print('Failed to create forecast. Check if you have at least 3 days of expenses.')
        return pd.DataFrame()


if __name__ == '__main__':
    forecast = train_cash_flow()
    if forecast.empty:
        raise SystemExit(1)

    table = Table(title='Expense forecast', header_style='bold light_steel_blue1')
    table.add_column('Date', justify='center')
    table.add_column('Projected expenses', justify='right')

    for row in forecast.itertuples(index=False):
        amount = f'{row.yhat1:,.2f}'.replace(',', ' ').replace('.', ',')
        table.add_row(row.ds.strftime('%d.%m.%Y'), f'{amount} zł')

    Console().print(table)
