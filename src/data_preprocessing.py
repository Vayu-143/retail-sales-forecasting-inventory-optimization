import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=["date"])

    # Cleaning
    df = df.drop_duplicates()
    df = df.dropna()

    return df