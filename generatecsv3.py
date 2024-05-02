import pandas as pd

# Load the previously fetched stock data
data = pd.read_csv("data_folder/apple_stock_data.csv")

# Calculate EMAs for s1 and s2
data['s1'] = data['Adj Close'].ewm(span=20, adjust=False).mean()  # EMA20
data['s2'] = data['Adj Close'].ewm(span=50, adjust=False).mean()  # EMA50

# Select only the relevant columns and save to new CSV
task3_data = data[['Date', 's1', 's2']]
task3_data.to_csv("task3.csv", index=False)