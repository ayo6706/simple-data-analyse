import pandas as pd

class SeriesCrossAnalyzer:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.data['crossabove'] = False
        self.data['crossbelow'] = False
    
    def analyze_crosses(self):
        s1 = self.data['s1']
        s2 = self.data['s2']
        
        # Calculate crossabove and crossbelow
        for i in range(1, len(s1)):
            if s1[i] > s2[i] and s1[i-1] <= s2[i-1]:
                self.data.at[i, 'crossabove'] = True
            if s1[i] < s2[i] and s1[i-1] >= s2[i-1]:
                self.data.at[i, 'crossbelow'] = True

        self.data['cross'] = self.data['crossabove'] | self.data['crossbelow']
        
        crossabove_count = self.data['crossabove'].sum()
        crossbelow_count = self.data['crossbelow'].sum()
        cross_count = self.data['cross'].sum()
        
        return crossabove_count, crossbelow_count, cross_count

    def get_trigger_datetimes(self):
        crossabove_dates = self.data[self.data['crossabove']]['Date'].tolist()
        crossbelow_dates = self.data[self.data['crossbelow']]['Date'].tolist()
        cross_dates = self.data[self.data['cross']]['Date'].tolist()
        
        return crossabove_dates, crossbelow_dates, cross_dates

# Example of usage
if __name__ == "__main__":
    analyzer = SeriesCrossAnalyzer("task3.csv")
    counts = analyzer.analyze_crosses()
    print("Crossabove count:", counts[0])
    print("Crossbelow count:", counts[1])
    print("Total crosses count:", counts[2])

    trigger_dates = analyzer.get_trigger_datetimes()
    print("Crossabove trigger dates:", trigger_dates[0])
    print("Crossbelow trigger dates:", trigger_dates[1])
    print("All crosses trigger dates:", trigger_dates[2])