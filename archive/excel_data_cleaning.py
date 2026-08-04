import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Shape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nData Types")
print(df.dtypes)
# Convert transaction_date into date format
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print("\nUpdated Data Types")
print(df.dtypes)

print("\nFirst 5 Rows")
print(df.head())

print("\nDate Range")
print(df["transaction_date"].min())
print(df["transaction_date"].max())
# Save cleaned dataset
df.to_csv("data/processed/cleaned_investor_transactions.csv", index=False)

print("\nCleaned dataset saved successfully.")

