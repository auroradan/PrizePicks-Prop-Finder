from collections import defaultdict
from statistics import mean
from MLBPropFinder.ODDS_MLB_SCRAPER import ODDS_MLB_SCRAPER
from MLBPropFinder.PRIZEPICKS_MLB_SCRAPER import PRIZEPICKS_MLB_SCRAPER

class MLBPropFinder():
    
    def __init__(self):
        self.mlb_data = ODDS_MLB_SCRAPER()
        self.prizepicks_data = PRIZEPICKS_MLB_SCRAPER().lines
        self.categories = []
        self.condense()
        self.getData()
        
    def condense(self):
        temp = set()
        for x in self.prizepicks_data: # (name, type, line, date)
            temp.add(x[1])
        self.categories = list(temp)
        self.pitcher_strikeouts_map = self.data_condenser(self.mlb_data.pitcher_strikeouts)
        self.total_bases_map = self.data_condenser(self.mlb_data.total_bases)
        self.hits_allowed_map = self.data_condenser(self.mlb_data.hits_allowed)
        self.pitcher_outs_map = self.data_condenser(self.mlb_data.pitcher_outs)
        self.batter_hits_runs_rbis_map = self.data_condenser(self.mlb_data.batter_hits_runs_rbis)

    def data_condenser(self, data):
        ans = defaultdict(list)
        for prop in data:
            key = (prop[0], prop[1], prop[2])
            ans[key].append(prop[3])
        return ans
    
    def getCategory(self, category):
        match category:
            case "Pitcher Strikeouts":
                return self.sieve("Pitcher Strikeouts", self.getPropsAverage(self.pitcher_strikeouts_map))
            case "Total Bases":
                return self.sieve("Total Bases", self.getPropsAverage(self.total_bases_map))
            case "Hits Allowed":
                return self.sieve("Hits Allowed", self.getPropsAverage(self.hits_allowed_map))
            case "Pitching Outs":
                return self.sieve("Pitching Outs", self.getPropsAverage(self.pitcher_outs_map))
            case "Hits+Runs+RBIs":
                return self.sieve("Hits+Runs+RBIs", self.getPropsAverage(self.batter_hits_runs_rbis_map))
            case _:
                pass
    
    def getPropsAverage(self, map):
        ans = []
        for key, odds in map.items():
            ans.append((key[0], key[1], key[2], round(mean(odds))))
        sorted_ans = sorted(ans, key=lambda x: x[3])
        return sorted_ans

    def sieve(self, category, map):
        ans = []
        hold = set()
        for x in self.prizepicks_data: # (name, type, line, date)
            name, type, line = x[0], x[1], x[2]
            if type == category:
                hold.add((name, line-0.5))
                hold.add((name, line))
                hold.add((name, line+0.5))
        for name, type, line, odds in map:
            temp = (name, line)
            if temp in hold and odds > -140 and odds < 140:
                ans.append((name, type, line, odds))
        return ans
        
    def getData(self):
        for category in self.categories:
            if category in {"Pitcher Strikeouts", "Total Bases", "Hits Allowed", "Pitching Outs", "Hits+Runs+RBIs"}:
                print("-------------------"+category+"-------------------")
                print(self.getCategory(category))
