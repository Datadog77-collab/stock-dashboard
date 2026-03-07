import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scope
)

client = gspread.authorize(creds)

spreadsheet = client.open("stock_data")

sheet = spreadsheet.sheet1

df = pd.read_csv("data/stock_price_timeseries.csv")

sheet.clear()

sheet.update([df.columns.values.tolist()] + df.values.tolist())

print("Google Sheets updated")
