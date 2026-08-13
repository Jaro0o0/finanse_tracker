import sys

from sympy import im

from ai.run_subprocess import run_forecast
from services.add_finanse import add_finanse

# SERVICES
from services import view_expenses
from services import forecast
from services import download_csv

from rich import  print







def main():
    while True:
        print('[light_steel_blue1]Welcome to Finanse App[/light_steel_blue1]')
        print('[light_steel_blue1]1: Add Expense[/light_steel_blue1]')
        print('[light_steel_blue1]2: View expenses[/light_steel_blue1]')
        print('[light_steel_blue1]3: AI expenses prognose[/light_steel_blue1]')
        print('[light_steel_blue1]4: Download expneses as CSV[/light_steel_blue1]')
        print('[light_steel_blue1]5: Exit[/light_steel_blue1] ')

        match(input('selec option: ')):
            case '1':
                add_finanse()
        
            case '2':
                view_expenses()
            # AI
            case '3':
                forecast(run_forecast)
            #DOWNLOAD_CSV
            case '4':
                download_csv()
            case '5':
                sys.exit()
            case _:
                print('wrong answear')



if __name__ == "__main__":
    main()
    
