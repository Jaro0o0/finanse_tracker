## 💵 Finanse Tracker
A personal expense tracking application built in Python. The program allows you to add expenses, review your history, analyze spending by month, and generate future expense forecasts using a local AI model.

📈 This project is actively being developed, and new features, improvements, and updates will be added regularly.


## ✨ Technologies

- `Python`
- `Pandas`
- `Rich`
- `sqlite3`
- `NeuralProphet`

## 🚀 Features

- `Track personal expenses`
- `forecast feature expenses`
- `Download data from local database to CSV file`

## 📊 How the Program Works

After launching the application, the menu appears with the following options:

1. Add Expense
2. View expenses
3. AI expenses prognose
4. Download expenses as CSV
5. Exit

Data is stored in the `FINANSE` table in a local SQLite database. In the forecasting section, the app reads data from the database, groups it by day, and creates a prediction using the NeuralProphet model.

## ▶️ Running the Project

From the project directory:

```bash
cd src
python main.py
```

## ⚠️ Forecast Note

The AI feature requires a sufficient amount of data. In the code, the application checks whether there are enough entries and, if needed, prompts the user to import data from a CSV file.




