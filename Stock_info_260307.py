import yfinance as yf
import pandas as pd

# =====================
# 対象銘柄
# =====================
symbols = {
    "JR_East": "9020.T",
    "JR_West": "9021.T",
    "JR_Central": "9022.T",
    "JR_Kyushu": "9142.T",
    "JAL": "9201.T",
    "ANA": "9202.T",
}

# =====================
# 市場データ
# =====================
market_index = {
    "Nikkei225": "^N225",
    "USDJPY": "JPY=X"
}

period = "5y"

result = []

# =====================
# 個別株データ取得
# =====================
for name, code in symbols.items():

    ticker = yf.Ticker(code)

    # -----------------
    # 株価取得
    # -----------------
    price_df = ticker.history(period=period)[["Close"]]

    if price_df.empty:
        print(f"{name}: 株価取得失敗")
        continue

    # タイムゾーン削除
    price_df.index = price_df.index.tz_localize(None)

    price_df = price_df.reset_index()
    price_df["Date"] = pd.to_datetime(price_df["Date"])

    # -----------------
    # 追加情報
    # -----------------
    shares = ticker.info.get("sharesOutstanding")

    price_df["Shares"] = shares

    if shares:
        price_df["MarketCap"] = price_df["Close"] * shares
    else:
        price_df["MarketCap"] = None

    price_df["Company"] = name
    price_df["Ticker"] = code
    price_df["Type"] = "Stock"

    result.append(price_df)

# =====================
# 日経平均・ドル円
# =====================
for name, code in market_index.items():

    ticker = yf.Ticker(code)

    df = ticker.history(period=period)[["Close"]]

    if df.empty:
        print(f"{name}: データ取得失敗")
        continue

    df.index = df.index.tz_localize(None)

    df = df.reset_index()
    df["Date"] = pd.to_datetime(df["Date"])

    df["Shares"] = None
    df["MarketCap"] = None

    df["Company"] = name
    df["Ticker"] = code
    df["Type"] = "Market"

    result.append(df)

# =====================
# 全データ結合
# =====================
final_df = pd.concat(result, ignore_index=True)

# =====================
# CSV出力
# =====================
final_df.to_csv(
    "data/stock_price_timeseries.csv",
    index=False,
    encoding="utf-8-sig"
)

print("CSV出力完了：stock_price_timeseries.csv")
print(final_df.head())