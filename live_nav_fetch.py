import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)
print("Status Code:", response.status_code)
json_data = response.json()
df = pd.DataFrame(json_data["data"])
print(df.head())
print(df.shape)
df.to_csv("data/raw/HDFC_Top100_NAV.csv", index=False)
print("CSV Saved Successfully")

import requests
import pandas as pd
import os
os.makedirs("data/raw", exist_ok=True)
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)
    if response.status_code == 200: 
        json_data = response.json()
        df = pd.DataFrame(json_data["data"])
        filename = f"data/raw/{fund_name}.csv"
        df.to_csv(filename, index=False)
        print(f"Downloaded {fund_name}")
    else:
        print(f"Failed to download {fund_name}")