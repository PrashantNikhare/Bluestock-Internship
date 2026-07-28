import pandas as pd

# Load both datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 70)
print("AMFI CODE VALIDATION")
print("=" * 70)

# Unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

print("\nTotal AMFI Codes in Fund Master")
print(len(fund_codes))

print("\nTotal AMFI Codes in NAV History")
print(len(nav_codes))

# Missing codes
missing_codes = fund_codes - nav_codes

print("\nMissing AMFI Codes")
print(missing_codes)

print("\nTotal Missing Codes")
print(len(missing_codes))