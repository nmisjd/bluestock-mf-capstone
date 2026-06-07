from sqlalchemy import create_engine
import pandas as pd

# Create SQLite database
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Load cleaned datasets
nav_df = pd.read_csv("data/processed/clean_nav_history.csv")
tx_df = pd.read_csv("data/processed/clean_transactions.csv")
perf_df = pd.read_csv("data/processed/clean_scheme_performance.csv")

# Load into SQLite
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
tx_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf_df.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database created successfully.")