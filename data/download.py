import yfinance as yf
import pandas as pd

def download_stock(ticker, period="1mo"):
    df=yf.download(
        ticker,
        period=period,
        auto_adjust=True,
        progress=False
    )
    if df.empty:
        raise ValueError(f"No data found for {ticker}")

    return df.reset_index()