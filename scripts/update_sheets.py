import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scope
)

client = gspread.authorize(creds)

spreadsheet = client.open("stock_price_timeseries")

sheet = spreadsheet.sheet1

# CSV読み込み
df = pd.read_csv("data/stock_price_timeseries.csv")

# ★ 重要：NaN対策
df = df.fillna("")

# シート更新sheet.clear()
sheet.update([df.columns.values.tolist()] + df.values.tolist())

print("Google Sheets updated")
