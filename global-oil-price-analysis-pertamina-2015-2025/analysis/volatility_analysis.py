import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/brent_oil_analysis.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Return"] = df["Close"].pct_change()

df["Volatility"] = df["Return"].rolling(30).std()

plt.figure(figsize=(14,6))

plt.plot(df["Date"], df["Volatility"])

plt.title("Oil Price Volatility (30-Day Rolling)")

plt.xlabel("Year")
plt.ylabel("Volatility")

plt.grid(True)

plt.savefig("visualization/charts/oil_volatility.png")

print("Volatility analysis completed")