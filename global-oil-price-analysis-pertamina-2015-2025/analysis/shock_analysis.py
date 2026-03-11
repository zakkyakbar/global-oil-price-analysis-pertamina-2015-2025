import pandas as pd

df = pd.read_csv("data/processed/brent_oil_analysis.csv")

df["Return"] = df["Close"].pct_change()

shock = df[abs(df["Return"]) > 0.05]

shock.to_csv("data/processed/oil_price_shocks.csv", index=False)

print("Shock events detected")

print(shock[["Date","Close","Return"]].head())