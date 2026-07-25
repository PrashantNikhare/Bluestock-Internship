import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

history = pd.DataFrame(data["data"])

history.to_csv("data/raw/HDFC_Top100_NAV.csv",index=False)

print(history.head())