from NonPropFinderSports.NCAAF.PRIZEPICKS_NCAAF_SCRAPER import PRIZEPICKS_NCAAF_SCRAPER
from collections import defaultdict
import pandas as pd

class NCAAF_PRIZEPICKS_EXCEL():
    
    def __init__(self):
        self.prizepicks_data = PRIZEPICKS_NCAAF_SCRAPER().lines
        self.categories = []
        self.data_dict = defaultdict(list)
        self.duplicates = defaultdict(set)
        self.condense()
        self.create_xlsx()
    
    def condense(self):
        temp = set()
        for data in self.prizepicks_data: # (name, type, line, date)
            name, type, line, date = data[0], data[1], data[2], data[3]
            temp.add(type)
            hold = (name, line, date, type)
            if hold not in self.duplicates[type]:
                self.duplicates[type].add(hold)
                self.data_dict[type].append(hold)
    
    def create_xlsx(self):
        combined_data = []
    
        for value in self.data_dict.values():
            combined_data.extend(value)
        
        df = pd.DataFrame(combined_data, columns=['Name', 'Line', 'Match Date', 'Stat Type'])
        
        with pd.ExcelWriter('EXCEL_PRIZEPICKS_DATA/ncaaf_prizepicks_data.xlsx', engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='All_Data')

        print("Excel file 'ncaaf_prizepicks_data.xlsx' created successfully.")
    