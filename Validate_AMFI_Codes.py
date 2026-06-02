import pandas as pd

fund_master = pd.read_csv("data/raw/fund_master.csv")
nav_history = pd.read_csv("data/raw/nav_history.csv")

# Check column names first
print("Fund Master Columns:")
print(fund_master.columns)

print("\nNAV History Columns:")
print(nav_history.columns)

# Ensure column exists
master_codes = set(fund_master["schemeCode"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("\nMissing Codes:")
print(missing_codes)

print("\nTotal Missing:", len(missing_codes))