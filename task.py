import yfinance as yf
import pandas as pd
import numpy as np

def fetch_data(symbol):
    # Fetch historical data from Yahoo Finance
    data = yf.download(symbol, start="2020-01-01", end="2022-01-01")
    return data

def calculate_ema(data, span):
    # Calculate Exponential Moving Average
    return data['Adj Close'].ewm(span=span, adjust=False).mean()

def trading_strategy(data):
    capital = 10000
    position = None  # 'long', 'short', or None
    entry_price = 0

    for i in range(1, len(data)):
        if data['ema20'].iloc[i] > data['ema50'].iloc[i] and data['ema20'].iloc[i-1] <= data['ema50'].iloc[i-1]:
            if position == 'short':
                # Close short position
                capital *= (entry_price / data['Adj Close'].iloc[i])
            # Open long position
            position = 'long'
            entry_price = data['Adj Close'].iloc[i]
        elif data['ema20'].iloc[i] < data['ema50'].iloc[i] and data['ema20'].iloc[i-1] >= data['ema50'].iloc[i-1]:
            if position == 'long':
                # Close long position
                capital *= (data['Adj Close'].iloc[i] / entry_price)
            # Open short position
            position = 'short'
            entry_price = data['Adj Close'].iloc[i]

    # Close any open position at the end
    if position == 'long':
        capital *= (data['Adj Close'].iloc[-1] / entry_price)
    elif position == 'short':
        capital *= (entry_price / data['Adj Close'].iloc[-1])

    return capital

def main():
    ticker = "AAPL"
    data = fetch_data(ticker)
    data['ema20'] = calculate_ema(data, 20)
    data['ema50'] = calculate_ema(data, 50)
    final_capital = trading_strategy(data)
    print(f"Final capital after trading {ticker}: ${final_capital:.2f}")

if __name__ == "__main__":
    main()