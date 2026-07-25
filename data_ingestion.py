import pandas as pd
import os

folder = "data/raw"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

for file in files:

    print("="*70)
    print(f"Dataset : {file}")
    print("="*70)

    df = pd.read_csv(os.path.join(folder, file))

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nSummary Statistics")
    print(df.describe())

    print("\nCategorical Summary")
    print(df.describe(include="object"))

    try:
        df = pd.read_csv(os.path.join(folder, file))
    except Exception as e:
        print(f"Error reading {file}: {e}")