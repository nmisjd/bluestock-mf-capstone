import pandas as pd
import os

folder = "data/raw"

all_data = []

for file in os.listdir(folder):

    if file.endswith("_nav.csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        # Extract AMFI code from filename mapping
        if "HDFC" in file:
            code = 125497
        elif "SBI" in file:
            code = 119551
        elif "ICICI" in file:
            code = 120503
        elif "Nippon" in file:
            code = 118632
        elif "Axis" in file:
            code = 119092
        elif "Kotak" in file:
            code = 120841
        else:
            code = None

        df["amfi_code"] = code

        all_data.append(df)

# Combine all NAV files
final_df = pd.concat(all_data, ignore_index=True)

# Save nav_history.csv
final_df.to_csv("data/raw/nav_history.csv", index=False)

print("nav_history.csv created successfully")
print(final_df.head())