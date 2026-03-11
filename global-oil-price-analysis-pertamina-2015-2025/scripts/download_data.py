import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta

def download_oil_data():

    print("Downloading Brent Oil data...")

    ticker = "BZ=F"

    end_date = datetime.today()
    start_date = end_date - timedelta(days=3650)

    df = yf.download(
        ticker,
        start=start_date.strftime("%Y-%m-%d"),
        end=end_date.strftime("%Y-%m-%d"),
        progress=False
    )

    df.reset_index(inplace=True)

    os.makedirs("data/raw", exist_ok=True)

    file_path = "data/raw/brent_oil_10years.csv"

    df.to_csv(file_path, index=False)

    print("\nDownload selesai")
    print("Dataset tersimpan di:", file_path)
    print("\nPreview data:\n")
    print(df.head())

if __name__ == "__main__":
    download_oil_data()