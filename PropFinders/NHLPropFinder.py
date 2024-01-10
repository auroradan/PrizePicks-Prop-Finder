from collections import defaultdict
from statistics import mean
from TheOddsAPIScraper.ODDS_NHL_SCRAPER import ODDS_NHL_SCRAPER
from PrizePicks.PRIZEPICKS_NHL_SCRAPER import PRIZEPICKS_NHL_SCRAPER

class NHLPropFinder():
    
    def __init__(self):
        self.nhl_data = ODDS_NHL_SCRAPER()
        self.prizepicks_data = PRIZEPICKS_NHL_SCRAPER().lines
        self.categories = []
        self.condense()
        self.getData()
        
    def condense(self):
        temp = set()
        for name, type, line in self.prizepicks_data:
            temp.add(type)
        self.categories = list(temp)
        self.saves_map = self.data_condenser(self.nhl_data.saves)
        self.shots_map = self.data_condenser(self.nhl_data.shots)
        self.points_map = self.data_condenser(self.nhl_data.points)
        self.blocks_map = self.data_condenser(self.nhl_data.blocks)

    def data_condenser(self, data):
        ans = defaultdict(list)
        for prop in data:
            key = (prop[0], prop[1], prop[2])
            ans[key].append(prop[3])
        return ans
    
    def getCategory(self, category):
        match category.lower():
            case "saves":
                return self.sieve("saves", self.getPropsAverage(self.saves_map))
            case "shots":
                return self.sieve("shots", self.getPropsAverage(self.shots_map))
            case "blocks":
                return self.sieve("blocks", self.getPropsAverage(self.blocks_map))
            case "points":
                return self.sieve("points", self.getPropsAverage(self.points_map))
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
                hold.add((name, line-0.5))
                hold.add((name, line))
                hold.add((name, line+0.5))
        for name, type, line, odds in map:
            temp = (name, line)
            if temp in hold:
                ans.append((name, type, line, odds))
        return ans
        
    def getData(self):
        for category in self.categories:
            print("-------------------"+category+"-------------------")
            print(self.getCategory(category))
