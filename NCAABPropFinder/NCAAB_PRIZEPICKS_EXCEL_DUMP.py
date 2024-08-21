from NCAABPropFinder.PRIZEPICKS_NCAAB_SCRAPER import PRIZEPICKS_NCAAB_SCRAPER
from collections import defaultdict
import pandas as pd

class NCAAB_PRIZEPICKS_CSV():
    
    def __init__(self):
        self.prizepicks_data = PRIZEPICKS_NCAAB_SCRAPER().lines
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
            hold = (name, line, date)
            if hold not in self.duplicates[type]:
                self.duplicates[type].add(hold)
                self.data_dict[type].append(hold)
    
    def create_xlsx(self):
        with pd.ExcelWriter('EXCEL_PRIZEPICKS_DATA/ncaab_prizepicks_data.xlsx', engine='xlsxwriter') as writer:
            for key, value in self.data_dict.items():
                df = pd.DataFrame(value, columns=['Name', 'Line', 'Datetime'])
                df.to_excel(writer, sheet_name=key, index=False)

        print("Excel file 'ncaab_prizepicks_data.xlsx' created successfully.")
    