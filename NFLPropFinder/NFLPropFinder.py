from collections import defaultdict
from statistics import mean
from NFLPropFinder.ODDS_NFL_SCRAPER import ODDS_NFL_SCRAPER
from NFLPropFinder.PRIZEPICKS_NFL_SCRAPER import PRIZEPICKS_NFL_SCRAPER

class NFLPropFinder():
    
    def __init__(self):
        self.nfl_data = ODDS_NFL_SCRAPER()
        self.prizepicks_data = PRIZEPICKS_NFL_SCRAPER().lines
        self.categories = []
        self.condense()
        self.getData()
        
    def condense(self):
        temp = set()
        for name, type, line in self.prizepicks_data:
            temp.add(type)
        self.categories = list(temp)
        self.passing_map = self.data_condenser(self.nfl_data.passing)
        self.receiving_map = self.data_condenser(self.nfl_data.receiving)
        self.attd_map = self.data_condenser(self.nfl_data.attd)
        self.rushing_map = self.data_condenser(self.nfl_data.rushing)

    def data_condenser(self, data):
        ans = defaultdict(list)
        for prop in data:
            key = (prop[0], prop[1], prop[2])
            ans[key].append(prop[3])
        return ans
    
    def getCategory(self, category):
        match category.lower():
            case "passing":
                return self.sieve("passing", self.getPropsAverage(self.passing_map))
            case "receiving":
                return self.sieve("receiving", self.getPropsAverage(self.receiving_map))
            case "attd":
                return self.sieve("attd", self.getPropsAverage(self.attd_map))
            case "rushing":
                return self.sieve("rushing", self.getPropsAverage(self.rushing_map))
            case _:
                print("invalid category")
    
    def getPropsAverage(self, map):
        ans = []
        for key, odds in map.items():
            ans.append((key[0], key[1], key[2], round(mean(odds))))
        sorted_ans = sorted(ans, key=lambda x: x[3])
        return sorted_ans

    def sieve(self, category, map):
        ans = []
        hold = set()
        for name, type, line in self.prizepicks_data:
            if type == category:
                hold.add((name, line))
        for name, type, line, odds in map:
            temp = (name, line)
            if temp in hold:
                ans.append((name, type, line, odds))
        return ans
        
    def getData(self):
        for category in self.categories:
            print("-------------------"+category+"-------------------")
            print(self.getCategory(category))
