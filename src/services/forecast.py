from pathlib import Path

from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.prompt import Prompt
from rich import print
from models import cursor,engine
import pandas as pd
from ai.run_subprocess import run_forecast
import threading
import time
    

def forecast():
    cursor.execute('SELECT * FROM FINANSE')
    expenses = cursor.fetchall()


    if len(expenses) < 30:
        while True:
            user_input = Prompt.ask(
                '[dark_orange]For minimum functionality, at least 30 expenses are required. Do you want to continue?[/]',
                choices=['y', 'n'],
                default='n',
            ).strip().lower()
            match(user_input):
                case 'y':

                    print('If you have a CSV file with expenses, you can import it to the database.')
                    user_input = input('Do you want to import expenses from a CSV file? (y/n): ').strip().lower()
                    match(user_input):
                        case 'y':
                            
                            csv_location = input('enter csv file location: ').strip()
                            try:
                                df = pd.read_csv(f'{csv_location}')
                                df.to_sql('FINANSE', con=engine, if_exists='append', index=False)
                                continue
                                
                            except FileNotFoundError:
                                print(f'file not found chceck your file location {csv_location} ')
                            except pd.errors.EmptyDataError:
                                print('CSV file is empty')
                        case 'n':
                            with Progress(
                                            SpinnerColumn(),
                                            TextColumn('[progress.description]{task.description}'),
                                            BarColumn(),
                                            TimeElapsedColumn(),
                                            transient=True,
                                        ) as progress:
                                            task_id = progress.add_task('Training model...', total=None)
                        
                                            result = {}
                        
                                            def _target():
                                                try:
                                                    result['output'] = run_forecast()
                                                except Exception as e:
                                                    result['output'] = f'Error during training: {e}'
                        
                                            thread = threading.Thread(target=_target, daemon=True)
                                            thread.start()
                        
                                            # Advance the progress bar while the training subprocess runs
                                            while thread.is_alive():
                                                progress.advance(task_id, 1)
                                                time.sleep(0.2)
                        
                                            thread.join()
                                            output = result.get('output')
                        
                                            print(output or 'The training script did not return a forecast.')

                                            break
                case 'n':
                    break
                    


      
