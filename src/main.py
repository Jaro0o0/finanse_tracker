import sys
from services.add_finanse import add_finanse

# SERVICES
from services.view_expenses import view_expenses
from services.forecast import forecast
from services.download_csv import download_csv

from rich import  print
from rich.align import Align
from rich.panel import Panel







def main():
    while True:
        menu = """[bold light_steel_blue1]1.[/] Add Expense
[bold light_steel_blue1]2.[/] View expenses
[bold light_steel_blue1]3.[/] AI expenses prognose
[bold light_steel_blue1]4.[/] Download expenses as CSV
[bold red]5.[/] Exit"""

        print(Panel(
            Align.center(menu),
            title='[bold light_steel_blue1]Welcome to Finanse Tracker[/]',
            border_style='light_steel_blue1',
            padding=(1, 4),
        ))

        match(input('select option: ')):
            case '1':
                add_finanse()
            #VIEW_EXPENSES
            case '2':
                view_expenses()
            # AI
            case '3':
                forecast()
            #DOWNLOAD_CSV
            case '4':
                download_csv()
            case '5':
                sys.exit()
            case _:
                print('wrong answear')



if __name__ == "__main__":
    main()
    
