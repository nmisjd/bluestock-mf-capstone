import requests
import pandas as pd

scheme_codes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_data = data.get("data", [])

    df = pd.DataFrame(nav_data)

    output_path = f"data/raw/{name}_nav.csv"

    df.to_csv(output_path, index=False)

    print(f"{name} saved successfully.")

