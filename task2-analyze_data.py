import pandas as pd

class StockDataAnalyzer:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
    
    def add_color_column(self):
        self.data['color'] = self.data.apply(lambda row: 'green' if row['close'] > row['open'] else 'red', axis=1)
        return self.data

# Example of usage
if __name__ == "__main__":
    analyzer = StockDataAnalyzer("data_folder/apple_stock_data.csv")
    data_with_colors = analyzer.add_color_column()
    print(data_with_colors.head())