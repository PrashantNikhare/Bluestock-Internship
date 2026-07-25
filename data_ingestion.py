import pandas as pd
import os

folder = "data/raw"

files = os.listdir(folder)

for file in files:

    if file.endswith(".csv"):

        print("\nFile Name :", file)

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("Shape :", df.shape)
        print("Columns :", df.columns)
        print("Data Types")
        print(df.dtypes)

        print("\nFirst 5 Rows")
        print(df.head())

        print("\nMissing Values")
        print(df.isnull().sum())
        print("\nColumns") 
        print(df.columns.tolist())
        print("\nDuplicate Rows") 
        print(df.duplicated().sum())
