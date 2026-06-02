import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

all_funds = []
offset = 0
limit = 1000

while True:
    url = f"https://api.mfapi.in/mf?limit={limit}&offset={offset}"

    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        break

    data = response.json()

    if not data:
        break

    all_funds.extend(data)

    print(f"Fetched {len(data)} records...")

    if len(data) < limit:
        break

    offset += limit

df = pd.DataFrame(all_funds)

df.to_csv("data/raw/fund_master.csv", index=False)

print("Saved:", len(df), "records")
print(df.head())