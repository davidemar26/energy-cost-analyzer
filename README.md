# Energy Cost Analyzer ⚡

A Python project for analyzing monthly energy consumption and costs from CSV data.

The project includes a command-line analysis tool and an interactive web dashboard built with Streamlit.

## Features

- Read energy data from a CSV file.
- Validate input data and detect invalid or duplicate months.
- Calculate total consumption, average consumption, and average costs.
- Identify the month with the highest energy cost.
- Analyze data using Pandas.
- Visualize monthly energy costs with charts.
- Filter dashboard data by month.
- Download filtered data as a CSV file.
- Run automated tests with pytest.

## Technologies

- Python
- Pandas
- Matplotlib
- Streamlit
- pytest
- CSV

## Project structure

```text
energy-cost-analyzer/
├── main.py
├── app.py
├── statistiche.py
├── validazione.py
├── test_statistiche.py
├── test_validazione.py
├── prova_pandas.py
├── risultati_energia.csv
├── README.md
└── .gitignore
```

## Requirements

- Python 3.13
- pip

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/davidemar26/energy-cost-analyzer
cd energy-cost-analyzer
```

Create a virtual environment:

```powershell
py -3.13 -m venv .venv
```

Install the required libraries:

```powershell
.\.venv\Scripts\python.exe -m pip install pandas matplotlib streamlit pytest
```

## Run the command-line analyzer

```powershell
.\.venv\Scripts\python.exe main.py
```

## Run the dashboard

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Streamlit will open the dashboard in your browser.

## Run the tests

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

## Learning goals

This project was developed to practice Python programming, input validation, automated testing, data analysis with Pandas, data visualization, and interactive dashboard development.

## Future improvements

- Improve error handling and data quality checks.
- Add more energy consumption and cost visualizations.
- Improve the dashboard layout and usability.