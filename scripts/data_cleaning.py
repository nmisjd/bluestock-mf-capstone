import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort values
df = df.sort_values(by=["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Validate NAV values
df = df[df["nav"] > 0]

# Save cleaned file
df.to_csv("data/processed/clean_nav_history.csv", index=False)

print("Cleaned Shape:", df.shape)
print("Cleaning completed successfully.")

tx_df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("\nTransactions Original Shape:", tx_df.shape)

# Convert dates
tx_df["transaction_date"] = pd.to_datetime(tx_df["transaction_date"])

# Standardize transaction types
tx_df["transaction_type"] = tx_df["transaction_type"].str.strip().str.title()

# Validate amount
tx_df = tx_df[tx_df["amount_inr"] > 0]

# Remove duplicates
tx_df = tx_df.drop_duplicates()

# Save cleaned transactions
tx_df.to_csv("data/processed/clean_transactions.csv", index=False)

print("Transactions Cleaned Shape:", tx_df.shape)

perf_df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\nPerformance Original Shape:", perf_df.shape)

# Validate numeric returns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio"
]

for col in numeric_cols:
    perf_df[col] = pd.to_numeric(perf_df[col], errors="coerce")

# Remove invalid rows
perf_df = perf_df.dropna()

# Validate expense ratio
perf_df = perf_df[
    (perf_df["expense_ratio_pct"] >= 0.1) &
    (perf_df["expense_ratio_pct"] <= 2.5)
]

# Save cleaned file
perf_df.to_csv("data/processed/clean_scheme_performance.csv", index=False)

print("Performance Cleaned Shape:", perf_df.shape)
