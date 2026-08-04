import pandas as pd
df = pd.read_csv("data/raw/02_nav_history.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())

df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)
df = df.sort_values(["amfi_code", "date"])

print(df["nav"].isnull().sum())
df["nav"] = df.groupby("amfi_code")["nav"].ffill()
print(df["nav"].isnull().sum())
print(df.duplicated().sum())
print(df.drop_duplicates())
print((df["nav"] <= 0).sum())
print(df[df["nav"] <= 0])
df = df[df["nav"] > 0]
print((df["nav"] <= 0).sum())
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)