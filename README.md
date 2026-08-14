# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project is a complete Mutual Fund Analytics solution developed using Python, SQLite, SQL, and Power BI.

The project covers the complete data analytics workflow starting from raw data collection to dashboard development.

The main objective is to analyse mutual fund performance, investor behaviour, SIP trends, portfolio allocation, and financial risk using different analytical techniques.

## Features

- ETL Pipeline using Python
- Data Cleaning and Validation
- SQLite Database
- SQL Queries
- Exploratory Data Analysis (EDA)
- Financial Performance Metrics
- Power BI Dashboard
- Advanced Analytics
- Mutual Fund Recommendation System

## Technology Stack

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Matplotlib
- Power BI
- Jupyter Notebook
- VS Code

## Folder Structure

```text
Bluestock project/
│
├── archive/
├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── database/
├── notebooks/
├── reports/
│   └── figures/
├── scripts/
├── sql/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── fund_master_analysis.py
├── README.md
├── requirements.txt
```

## Installation

Clone the repository

```bash
git clone https://github.com/PrashantNikhare/Bluestock-Internship
```

Go to project folder

```bash
cd Bluestock project
```

Install dependencies

```bash
pip install -r requirements.txt
```
## How to Run

### Run ETL Pipeline

```bash
python data_ingestion.py
```

### Clean Data

```bash
python scripts/clean_data.py
```

### Load Data into SQLite

```bash
python scripts/load_to_sqlite.py
```

### Generate Analysis

```bash
python fund_master_analysis.py
```

### Fetch Live NAV

```bash
python live_nav_fetch.py
```

### Run Recommendation System

```bash
python scripts/recommender.py
```

## Project Outputs

The project generates the following outputs:

- Cleaned CSV files
- SQLite Database
- Financial Performance Metrics
- EDA Charts
- Power BI Dashboard
- Final Report
- Project Presentation


## Dashboard Preview

The Power BI dashboard contains four interactive pages.

- Industry Overview
- Fund Performance
- Investor Analytics
- SIP & Market Trends

Dashboard File

```text
dashboard/bluestock_mf_dashboard.pbix
```

## Datasets Used

- Fund Master
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

## Project Workflow

```text
Raw CSV Files
      │
      ▼
Data Cleaning
      │
      ▼
SQLite Database
      │
      ▼
EDA
      │
      ▼
Performance Analytics
      │
      ▼
Power BI Dashboard
      │
      ▼
Final Report
```

## Author

Prashant Nikhare

Data Analytics Intern

Bluestock Mutual Fund Analytics Capstone

GitHub : https://github.com/PrashantNikhare/Bluestock-Internship

## License

This project was developed for academic and internship learning purposes.