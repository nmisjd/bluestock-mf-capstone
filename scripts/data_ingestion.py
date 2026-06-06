import pandas as pd
import os

DATA_FOLDER = "data/raw"

files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

for file in files:

    path = os.path.join(DATA_FOLDER, file)

    print("=" * 60)
    print(f"FILE: {file}")

    df = pd.read_csv(path)

    print("\nSHAPE:")
    print(df.shape)

    print("\nDTYPES:")
    print(df.dtypes)

    print("\nHEAD:")
    print(df.head())

    print("\nMISSING VALUES:")
    print(df.isnull().sum())

    print("=" * 60)