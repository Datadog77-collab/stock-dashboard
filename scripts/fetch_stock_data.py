import yfinance as yf
import pandas as pd
import os

# =====================
# データ保存フォルダ作成
# =====================
os.makedirs("data", exist_ok=True)

# =====================
# 対象銘柄
# =====================
symbols = {
    # ===== 水産・農林 =====
    "Nissui": "1332.T",
    "Maruha_Nichiro": "1333.T",
    "Nippon_Suisan": "1332.T",
    "Oisix": "3182.T",
    "Hokuto": "1379.T",

    # ===== 鉱業 =====
    "INPEX": "1605.T",
    "Japan_Petroleum": "1662.T",
    "Kanto_Natural_Gas": "1663.T",

    # ===== 建設 =====
    "Obayashi": "1802.T",
    "Kajima": "1812.T",
    "Shimizu": "1803.T",
    "Taisei": "1801.T",
    "Haseko": "1808.T",

    # ===== 食料品 =====
    "Kirin": "2503.T",
    "Asahi": "2502.T",
    "Ajinomoto": "2802.T",
    "Kikkoman": "2801.T",
    "Meiji": "2269.T",

    # ===== 繊維製品 =====
    "Toray": "3402.T",
    "Teijin": "3401.T",
    "Toyobo": "3101.T",
    "Gunze": "3002.T",

    # ===== パルプ・紙 =====
    "Oji": "3861.T",
    "Nippon_Paper": "3863.T",
    "Hokuetsu": "3865.T",

    # ===== 化学 =====
    "ShinEtsu": "4063.T",
    "Mitsubishi_Chemical": "4188.T",
    "Sumitomo_Chemical": "4005.T",
    "Asahi_Kasei": "3407.T",
    "Kao": "4452.T",

    # ===== 医薬品 =====
    "Takeda": "4502.T",
    "Astellas": "4503.T",
    "Daiichi_Sankyo": "4568.T",
    "Otsuka": "4578.T",
    "Eisai": "4523.T",

    # ===== 石油・石炭 =====
    "ENEOS": "5020.T",
    "Idemitsu": "5019.T",
    "Cosmo": "5021.T",

    # ===== ゴム製品 =====
    "Bridgestone": "5108.T",
    "Sumitomo_Rubber": "5110.T",
    "Yokohama_Rubber": "5101.T",

    # ===== ガラス・土石 =====
    "AGC": "5201.T",
    "Nippon_Electric_Glass": "5214.T",
    "Taiheiyo_Cement": "5233.T",
    "TOTO": "5332.T",

    # ===== 鉄鋼 =====
    "Nippon_Steel": "5401.T",
    "JFE": "5411.T",
    "Kobe_Steel": "5406.T",

    # ===== 非鉄金属 =====
    "Sumitomo_Metal": "5713.T",
    "Mitsui_Mining": "5706.T",
    "DOWA": "5714.T",
    "Furukawa": "5715.T",

    # ===== 機械 =====
    "SMC": "6273.T",
    "Daikin": "6367.T",
    "Kubota": "6326.T",
    "Komatsu": "6301.T",
    "Hitachi_Construction": "6305.T",

    # ===== 電気機器 =====
    "Sony": "6758.T",
    "Hitachi": "6501.T",
    "Panasonic": "6752.T",
    "Keyence": "6861.T",
    "Nintendo": "7974.T",

    # ===== 輸送用機器 =====
    "Toyota": "7203.T",
    "Honda": "7267.T",
    "Denso": "6902.T",
    "Suzuki": "7269.T",
    "Subaru": "7270.T",

    # ===== 精密機器 =====
    "Olympus": "7733.T",
    "Terumo": "4543.T",
    "Hoya": "7741.T",
    "Shimadzu": "7701.T",

    # ===== その他製品 =====
    "Bandai_Namco": "7832.T",
    "Sony_Group": "6758.T",
    "Nintendo_Alt": "7974.T",

    # ===== 電気・ガス =====
    "TEPCO": "9501.T",
    "Kansai_Electric": "9503.T",
    "Chubu_Electric": "9502.T",
    "Tokyo_Gas": "9531.T",
    "Osaka_Gas": "9532.T",

    # ===== 陸運 =====
    "JR_East": "9020.T",
    "JR_West": "9021.T",
    "JR_Central": "9022.T",
    "Yamato": "9064.T",
    "Sagawa": "9143.T",

    # ===== 海運 =====
    "NYK": "9101.T",
    "MOL": "9104.T",
    "KLine": "9107.T",

    # ===== 空運 =====
    "JAL": "9201.T",
    "ANA": "9202.T",

    # ===== 倉庫・運輸関連 =====
    "Mitsui_Warehouse": "9301.T",
    "Sumitomo_Warehouse": "9303.T",
    "Mitsubishi_Logistics": "9301.T",

    # ===== 情報・通信 =====
    "NTT": "9432.T",
    "SoftBank": "9434.T",
    "KDDI": "9433.T",
    "Rakuten": "4755.T",
    "Z_Holdings": "4689.T",

    # ===== 卸売 =====
    "Mitsubishi_Corp": "8058.T",
    "Mitsui": "8031.T",
    "Itochu": "8001.T",
    "Sumitomo_Corp": "8053.T",
    "Marubeni": "8002.T",

    # ===== 小売 =====
    "Fast_Retailing": "9983.T",
    "Seven_i": "3382.T",
    "Aeon": "8267.T",
    "PanPacific": "7532.T",
    "Nitori": "9843.T",

    # ===== 銀行 =====
    "MUFG": "8306.T",
    "SMFG": "8316.T",
    "Mizuho": "8411.T",
    "Resona": "8308.T",

    # ===== 証券・商品先物 =====
    "Nomura": "8604.T",
    "Daiwa": "8601.T",
    "SBI": "8473.T",

    # ===== 保険 =====
    "Tokio_Marine": "8766.T",
    "MS_AD": "8725.T",
    "Sompo": "8630.T",
    "Daiichi_Life": "8750.T",

    # ===== 不動産 =====
    "Mitsui_Fudosan": "8801.T",
    "Mitsubishi_Estate": "8802.T",
    "Sumitomo_Realty": "8830.T",
    "Tokyu_Land": "3289.T"
}


# =====================
# 市場データ
# =====================
market_index = {
    "Nikkei225": "^N225",
    "USDJPY": "JPY=X"
}

period = "10y"

result = []

# =====================
# 個別株データ取得
# =====================
for name, code in symbols.items():

    print(f"Fetching: {name}")

    ticker = yf.Ticker(code)

    try:
        price_df = ticker.history(period=period)[["Close"]]
    except Exception as e:
        print(f"{name}: 株価取得エラー {e}")
        continue

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
    try:
        shares = ticker.info.get("sharesOutstanding")
    except:
        shares = None

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
# 市場データ取得
# =====================
for name, code in market_index.items():

    print(f"Fetching: {name}")

    ticker = yf.Ticker(code)

    try:
        df = ticker.history(period=period)[["Close"]]
    except Exception as e:
        print(f"{name}: データ取得エラー {e}")
        continue

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

# 列順整理（Tableau用）
final_df = final_df[
    [
        "Date",
        "Company",
        "Ticker",
        "Type",
        "Close",
        "Shares",
        "MarketCap"
    ]
]

# =====================
# CSV出力
# =====================
output_path = "data/stock_price_timeseries.csv"

final_df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print("CSV出力完了")
print(output_path)
print(final_df.head())
