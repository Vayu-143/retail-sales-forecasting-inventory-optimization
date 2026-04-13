def create_features(df):
    df = df.sort_values("date")

    # Lag features
    df["lag_1"] = df["qty_sold"].shift(1)
    df["lag_7"] = df["qty_sold"].shift(7)

    # Rolling features
    df["rolling_mean_3"] = df["qty_sold"].rolling(3).mean()

    # Date features
    df["day_of_week"] = df["date"].dt.dayofweek

    # Drop NaN
    df = df.dropna()

    return df