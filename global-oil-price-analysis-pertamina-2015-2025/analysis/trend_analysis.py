import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/brent_oil_analysis.csv")

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(14,7))

plt.plot(df["Date"], df["Close"], label="Oil Price")

plt.plot(df["Date"], df["MA30"], label="MA30")

plt.plot(df["Date"], df["MA90"], label="MA90")

plt.title("Oil Price Trend with Moving Average")

plt.xlabel("Year")
plt.ylabel("Price USD")

plt.legend()

plt.grid(True)

plt.savefig("visualization/charts/oil_trend_analysis.png")

print("Trend analysis completed")