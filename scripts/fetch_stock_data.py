import yfinance as yf
import pandas as pd
from datetime import datetime

tickers = ["AAPL", "MSFT", "NVDA", "TSLA"]

data_list = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d", interval="1h")

    hist["ticker"] = ticker
    hist.reset_index(inplace=True)

    data_list.append(hist)

df = pd.concat(data_list)

df = df[["Datetime", "ticker", "Open", "High", "Low", "Close", "Volume"]]

df.to_csv("data/stock_price_timeseries.csv", index=False)

print("CSV updated")
