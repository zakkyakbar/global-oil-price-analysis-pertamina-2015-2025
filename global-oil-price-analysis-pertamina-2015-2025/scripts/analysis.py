import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():

    file_path = "data/raw/brent_oil_10years.csv"

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])

    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    df = df.sort_values("Date")

    return df

def add_indicators(df):

    df["MA30"] = df["Close"].rolling(window=30).mean()

    df["MA90"] = df["Close"].rolling(window=90).mean()

    return df

def show_summary(df):

    print("\n===== OIL PRICE SUMMARY =====")

    print("Total Data :", len(df))

    print("Start Date :", df["Date"].min())

    print("End Date   :", df["Date"].max())

    print("\nPrice Statistics")

    print("Highest Price :", df["Close"].max())

    print("Lowest Price  :", df["Close"].min())

    print("Average Price :", round(df["Close"].mean(),2))

def save_analysis(df):

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv("data/processed/brent_oil_analysis.csv", index=False)

    print("\nAnalysis dataset saved to data/processed/")

def create_chart(df):

    os.makedirs("visualization/charts", exist_ok=True)

    plt.figure(figsize=(14,7))

    plt.plot(df["Date"], df["Close"], label="Oil Price")

    plt.plot(df["Date"], df["MA30"], label="MA30")

    plt.plot(df["Date"], df["MA90"], label="MA90")

    plt.title("Brent Oil Price Trend (10 Years)")

    plt.xlabel("Year")

    plt.ylabel("Price USD")

    plt.legend()

    plt.grid(True)

    plt.savefig("visualization/charts/oil_price_trend.png")

    print("Chart saved to visualization/charts/")

if __name__ == "__main__":

    df = load_data()

    df = add_indicators(df)

    show_summary(df)

    save_analysis(df)

    create_chart(df)