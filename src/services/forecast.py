from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from models import cursor
import pandas as pd
from ai.run_subprocess import run_forecast
import re


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
    

    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        BarColumn(),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task_id = progress.add_task('Trenowanie modelu...', total=100)

        def _on_line(line: str):
            # Try to parse epoch progress like "12/100" or "Epoch 12/100"
            try:
                if 'epoch' in line.lower() or '/' in line:
                    m = re.search(r"(\d+)\s*/\s*(\d+)", line)
                    if m:
                        curr = int(m.group(1))
                        tot = int(m.group(2))
                        # update total (in case it's different)
                        progress.update(task_id, total=tot)
                        progress.update(task_id, completed=curr, description=f'Trenowanie modelu... {curr}/{tot}')
            except Exception:
                pass

        output = run_forecast(on_line=_on_line)

    print(output or 'Skrypt treningu nie zwrócił prognozy.')
