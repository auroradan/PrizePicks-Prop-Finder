from NFLPropFinder.PRIZEPICKS_NFL_SCRAPER import PRIZEPICKS_NFL_SCRAPER
from collections import defaultdict
import pandas as pd

class NFL_PRIZEPICKS_CSV():
    
    def __init__(self):
        self.prizepicks_data = PRIZEPICKS_NFL_SCRAPER().lines
        self.categories = []
        self.data_dict = defaultdict(list)
        self.duplicates = defaultdict(set)
        self.condense()
        self.create_xlsx()
    
    def condense(self):
        temp = set()
        for name, type, line in self.prizepicks_data:
            temp.add(type)
            hold = (name, line)
            if hold not in self.duplicates[type]:
                self.duplicates[type].add(hold)
                self.data_dict[type].append(hold)
    
    def create_xlsx(self):
        with pd.ExcelWriter('CSV_PRIZEPICKS_DATA/nfl_prizepicks_data.xlsx', engine='xlsxwriter') as writer:
            for key, value in self.data_dict.items():
                df = pd.DataFrame(value, columns=['Name', 'Line'])
                df.to_excel(writer, sheet_name=key, index=False)

        print("Excel file 'nfl_prizepicks_data.xlsx' created successfully.")
    