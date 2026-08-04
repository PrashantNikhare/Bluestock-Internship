import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed"
FIGURES_PATH = BASE_DIR / "reports" / "figures"

fund_master = pd.read_csv(DATA_PATH / "01_fund_master_cleaned.csv")
nav_history = pd.read_csv(DATA_PATH / "02_nav_history_cleaned.csv")

FIGURES_PATH.mkdir(parents=True, exist_ok=True)

print("="*60)
print("FUND MASTER")
print("="*60)

print(fund_master.shape)
fund_master.info()
print(fund_master.head())

print("="*60)
print("NAV HISTORY")
print("="*60)

print(nav_history.shape)
nav_history.info()
print(nav_history.head())

print("\nMissing Values - Fund Master")
print(fund_master.isnull().sum())

print("\nMissing Values - NAV History")
print(nav_history.isnull().sum())

print("\nDuplicate Rows")

print("Fund Master :", fund_master.duplicated().sum())
print("NAV History :", nav_history.duplicated().sum())

print("\nSummary Statistics")

print(fund_master.describe(include="all"))

print(nav_history.describe())

print("\nUnique Fund Houses")
print(fund_master["fund_house"].nunique())

print("\nCategories")
print(fund_master["category"].value_counts())

print("\nPlans")
print(fund_master["plan"].value_counts())

print("Risk Category")
print(fund_master["risk_category"].value_counts())

print("\nNAV Statistics")

print("Minimum NAV :", nav_history["nav"].min())
print("Maximum NAV :", nav_history["nav"].max())
print("Average NAV :", nav_history["nav"].mean())

plt.figure(figsize=(8,5))

fund_master["category"].value_counts().plot(kind="bar")

plt.title("Funds by Category")
plt.xlabel("Category")
plt.ylabel("Number of Funds")

plt.tight_layout()

plt.savefig(FIGURES_PATH / "01_category_distribution.png", dpi=300)

plt.close()

plt.figure(figsize=(8,5))

fund_master["risk_category"].value_counts().plot(kind="bar")

plt.title("Risk Category Distribution")
plt.xlabel("Risk Category")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig(FIGURES_PATH / "02_risk_category_distribution.png", dpi=300)

plt.close()

plt.figure(figsize=(6,6))

fund_master["plan"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Plan Distribution")

plt.savefig(FIGURES_PATH / "03_plan_distribution.png", dpi=300)

plt.close()

plt.figure(figsize=(10,5))

fund_master["fund_house"].value_counts().plot(kind="bar")

plt.title("Top Fund Houses")
plt.xlabel("Fund House")
plt.ylabel("Number of Funds")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(FIGURES_PATH / "04_fund_houses.png", dpi=300)

plt.close()

plt.figure(figsize=(8,5))

plt.hist(fund_master["expense_ratio_pct"], bins=10)

plt.title("Expense Ratio Distribution")
plt.xlabel("Expense Ratio (%)")
plt.ylabel("Number of Funds")

plt.tight_layout()

plt.savefig(FIGURES_PATH / "05_expense_ratio_distribution.png", dpi=300)

plt.close()

plt.figure(figsize=(8,5))

plt.hist(fund_master["exit_load_pct"], bins=10)

plt.title("Exit Load Distribution")
plt.xlabel("Exit Load (%)")
plt.ylabel("Number of Funds")

plt.tight_layout()

plt.savefig(FIGURES_PATH / "06_exit_load_distribution.png", dpi=300)

plt.close()

plt.figure(figsize=(8,5))

plt.hist(nav_history["nav"], bins=30)

plt.title("NAV Distribution")
plt.xlabel("NAV")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(FIGURES_PATH / "07_nav_distribution.png", dpi=300)

plt.close()

nav_history["date"] = pd.to_datetime(nav_history["date"])
daily_nav = nav_history.groupby("date")["nav"].mean()
plt.figure(figsize=(12,5))

plt.plot(daily_nav.index, daily_nav.values)

plt.title("Average NAV Trend")
plt.xlabel("Date")
plt.ylabel("Average NAV")

plt.tight_layout()

plt.savefig(FIGURES_PATH / "08_average_nav_trend.png", dpi=300)
plt.close()

plt.figure(figsize=(12,5))

top_expense = fund_master.sort_values(
    by="expense_ratio_pct",
    ascending=False
).head(10)

plt.bar(top_expense["scheme_name"], top_expense["expense_ratio_pct"])

plt.title("Top 10 Funds by Expense Ratio")
plt.xlabel("Scheme Name")
plt.ylabel("Expense Ratio (%)")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig(FIGURES_PATH / "09_top_expense_ratio.png", dpi=300)

plt.close()

plt.figure(figsize=(10,5))

top_sip = fund_master.sort_values(
    by="min_sip_amount"
).head(10)

plt.bar(top_sip["scheme_name"], top_sip["min_sip_amount"])

plt.title("Minimum SIP Amount")
plt.xlabel("Scheme")
plt.ylabel("Minimum SIP")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig(FIGURES_PATH / "10_minimum_sip.png", dpi=300)

plt.close()

plt.figure(figsize=(12,5))

fund_master["fund_manager"].value_counts().head(10).plot(kind="bar")

plt.title("Top Fund Managers")
plt.xlabel("Fund Manager")
plt.ylabel("Number of Schemes")

plt.tight_layout()

plt.savefig(FIGURES_PATH / "11_fund_manager_distribution.png", dpi=300)

plt.close()

plt.figure(figsize=(8,5))

plt.boxplot(nav_history["nav"])

plt.title("NAV Box Plot")

plt.tight_layout()

plt.savefig(FIGURES_PATH / "12_nav_boxplot.png", dpi=300)

plt.close()

print("\n" + "="*60)
print("EDA SUMMARY")
print("="*60)

print(f"Total Funds           : {len(fund_master)}")
print(f"Total NAV Records     : {len(nav_history)}")
print(f"Fund Houses           : {fund_master['fund_house'].nunique()}")
print(f"Fund Managers         : {fund_master['fund_manager'].nunique()}")
print(f"Categories            : {fund_master['category'].nunique()}")
print(f"Average Expense Ratio : {fund_master['expense_ratio_pct'].mean():.2f}%")
print(f"Average NAV           : {nav_history['nav'].mean():.2f}")

print("="*60)
print("All graphs saved successfully.")
print("="*60)


