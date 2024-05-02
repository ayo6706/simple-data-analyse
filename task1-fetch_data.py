import yfinance as yf
import pandas as pd
import os

class YahooFinanceData:
    def __init__(self, symbol, start_date, end_date, interval='1d'):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval

    def fetch(self):
        data = yf.download(self.symbol, start=self.start_date, end=self.end_date, interval=self.interval)
        # Make column names lowercase
        data.columns = [col.lower() for col in data.columns]
        # Remove unnecessary columns
        data = data.drop(columns=['adj close'], errors='ignore')
        return data

    def save_data(self, data, folder_name, file_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        data.to_csv(f"{folder_name}/{file_name}.csv")

# Example of usage
if __name__ == "__main__":
    yf_data = YahooFinanceData("AAPL", "2022-01-01", "2022-12-31", "1d")
    data = yf_data.fetch()
    yf_data.save_data(data, "data_folder", "apple_stock_data")