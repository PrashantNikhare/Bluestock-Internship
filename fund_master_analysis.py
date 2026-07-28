import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 70)
print("Fund Master Dataset")
print("=" * 70)

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nUnique Fund Houses")
print(df["fund_house"].unique())

print("\nTotal Fund Houses")
print(df["fund_house"].nunique())

print("\nCategories")
print(df["category"].unique())

print("\nSub Categories")
print(df["sub_category"].unique())

print("\nRisk Categories")
print(df["risk_category"].unique())

print("\nSEBI Category Codes")
print(df["sebi_category_code"].unique())

print("\nFirst 10 AMFI Codes")
print(df["amfi_code"].head(10))