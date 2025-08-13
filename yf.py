import yfinance as yf
import pandas as pd
import os
from datetime import datetime

# --- Settings ---
ticker_symbol = "AAPL"
start_date = "2024-01-01"
end_date   = "2024-12-31"
save_folder = r"C:\Users\User\Desktop\Data\Apple"

# --- Download Data ---
print(f"Downloading {ticker_symbol} stock data from {start_date} to {end_date}...")
aapl = yf.download(ticker_symbol, start=start_date, end=end_date)

# --- Create timestamped filename ---
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"{ticker_symbol}_2024_{timestamp}.csv"
file_path = os.path.join(save_folder, file_name)

# --- Save to CSV ---
aapl.to_csv(file_path)
print(f"Saved: {file_path}")

# --- Optional preview ---
print(aapl)