import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_PATH = BASE_DIR / "data" / "processed"

DB_PATH = BASE_DIR / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

print("Database Connected Successfully!")

# ===============================
# Load 01_fund_master
# ===============================

fund_master = pd.read_csv(PROCESSED_PATH / "01_fund_master_cleaned.csv")

fund_master.to_sql(
    "fund_master",
    engine,
    if_exists="replace",
    index=False
)

print(f"✓ fund_master loaded ({len(fund_master)} rows)")

# ===============================
# Load 02_nav_history
# ===============================

nav_history = pd.read_csv(PROCESSED_PATH / "02_nav_history_cleaned.csv")

nav_history.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

print(f"✓ nav_history loaded ({len(nav_history)} rows)")

# ===============================
# Load 03_aum_by_fund_house
# ===============================

aum_by_fund_house = pd.read_csv(PROCESSED_PATH / "03_aum_by_fund_house_cleaned.csv")
aum_by_fund_house.to_sql("aum_by_fund_house", engine, if_exists="replace", index=False)
print(f"✓ aum_by_fund_house loaded ({len(aum_by_fund_house)} rows)")

# ===============================
# Load 04_monthly_sip_inflows
# ===============================

monthly_sip_inflows = pd.read_csv(PROCESSED_PATH / "04_monthly_sip_inflows_cleaned.csv")
monthly_sip_inflows.to_sql("monthly_sip_inflows", engine, if_exists="replace", index=False)
print(f"✓ monthly_sip_inflows loaded ({len(monthly_sip_inflows)} rows)")

# ===============================
# Load 05_category_inflows
# ===============================

category_inflows = pd.read_csv(PROCESSED_PATH / "05_category_inflows_cleaned.csv")
category_inflows.to_sql("category_inflows", engine, if_exists="replace", index=False)
print(f"✓ category_inflows loaded ({len(category_inflows)} rows)")

# ===============================
# Load 06_industry_folio_count
# ===============================

industry_folio_count = pd.read_csv(PROCESSED_PATH / "06_industry_folio_count_cleaned.csv")
industry_folio_count.to_sql("industry_folio_count", engine, if_exists="replace", index=False)
print(f"✓ industry_folio_count loaded ({len(industry_folio_count)} rows)")

# ===============================
# Load 07_scheme_performance
# ===============================

scheme_performance = pd.read_csv(PROCESSED_PATH / "07_scheme_performance_cleaned.csv")
scheme_performance.to_sql("scheme_performance", engine, if_exists="replace", index=False)
print(f"✓ scheme_performance loaded ({len(scheme_performance)} rows)")

# ===============================
# Load 08_investor_transactions
# ===============================

investor_transactions = pd.read_csv(PROCESSED_PATH / "08_investor_transactions_cleaned.csv")
investor_transactions.to_sql("investor_transactions", engine, if_exists="replace", index=False)
print(f"✓ investor_transactions loaded ({len(investor_transactions)} rows)")

# ===============================
# Load 09_portfolio_holdings
# ===============================

portfolio_holdings = pd.read_csv(PROCESSED_PATH / "09_portfolio_holdings_cleaned.csv")
portfolio_holdings.to_sql("portfolio_holdings", engine, if_exists="replace", index=False)
print(f"✓ portfolio_holdings loaded ({len(portfolio_holdings)} rows)")

# ===============================
# Load 10_benchmark_indices
# ===============================

benchmark_indices = pd.read_csv(PROCESSED_PATH / "10_benchmark_indices_cleaned.csv")
benchmark_indices.to_sql("benchmark_indices", engine, if_exists="replace", index=False)
print(f"✓ benchmark_indices loaded ({len(benchmark_indices)} rows)")

print("\n🎉 All datasets loaded into SQLite successfully!")