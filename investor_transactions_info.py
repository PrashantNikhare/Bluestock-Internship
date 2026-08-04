import pandas as pd;
df = pd.read_csv("data/raw/08_investor_transactions.csv")
print("=" * 70)
print("INVESTOR TRANSACTIONS DATASET")
print("=" * 70)

print("\nShape")
print(df.shape)
print("\nColumns")
print(df.columns.tolist())
print("First 5 Rows")
print(df.head())
