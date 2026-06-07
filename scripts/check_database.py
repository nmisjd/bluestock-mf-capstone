from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    engine
)

print(tables)