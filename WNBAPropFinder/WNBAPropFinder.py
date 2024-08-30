from collections import defaultdict
from WNBAPropFinder.ODDS_WNBA_SCRAPER import ODDS_WNBA_SCRAPER
from WNBAPropFinder.PRIZEPICKS_WNBA_SCRAPER import PRIZEPICKS_WNBA_SCRAPER
from BookWeight import BookWeight


class WNBAPropFinder():
    
    def __init__(self):
        self.nba_data = ODDS_WNBA_SCRAPER()
        self.prizepicks_data = PRIZEPICKS_WNBA_SCRAPER().lines
        self.book_to_weight = BookWeight().getBookToWeight()
        self.private_books = BookWeight().getPrivateBooks()
        self.categories = []
        self.condense()
        self.getData()
        
    def condense(self):
        temp = set()
        for x in self.prizepicks_data: # (name, type, line, date)
            temp.add(x[1])
        self.categories = list(temp)
        self.points_map = self.data_condenser(self.nba_data.points)
        self.rebounds_map = self.data_condenser(self.nba_data.rebounds)
        self.assists_map = self.data_condenser(self.nba_data.assists)
        self.threes_map = self.data_condenser(self.nba_data.threes)
        self.blocks_map = self.data_condenser(self.nba_data.blocks)
        self.steals_map = self.data_condenser(self.nba_data.steals)
        self.pra_map = self.data_condenser(self.nba_data.pra)
        self.pr_map = self.data_condenser(self.nba_data.pr)
        self.pa_map = self.data_condenser(self.nba_data.pa)
        self.ra_map = self.data_condenser(self.nba_data.ra)
        

    def data_condenser(self, data):
        ans = defaultdict(list)
        for prop in data:
            key = (prop[0], prop[1], prop[2])
            ans[key].append((prop[3], prop[4]))
        return ans
    
    def getCategory(self, category):
        match category:
            case "Points":
                return self.sieve("Points", self.getPropsAverage(self.points_map))
            case "Rebounds":
                return self.sieve("Rebounds", self.getPropsAverage(self.rebounds_map))
            case "Assists":
                return self.sieve("Assists", self.getPropsAverage(self.assists_map))
            case "3-PT Made":
                return self.sieve("3-PT Made", self.getPropsAverage(self.threes_map))
            case "Blocked Shots":
                return self.sieve("Blocked Shots", self.getPropsAverage(self.blocks_map))
            case "Steals":
                return self.sieve("Steals", self.getPropsAverage(self.steals_map))
            case "Pts+Rebs+Asts":
                return self.sieve("Pts+Rebs+Asts", self.getPropsAverage(self.pra_map))
            case "Pts+Rebs":
                return self.sieve("Pts+Rebs", self.getPropsAverage(self.pr_map))
            case "Pts+Asts":
                return self.sieve("Pts+Asts", self.getPropsAverage(self.pa_map))
            case "Rebs+Asts":
                return self.sieve("Rebs+Asts", self.getPropsAverage(self.ra_map))
            case _:
                pass
    
    def getPropsAverage(self, map):
        ans = []
        for key, data in map.items():
            ans.append((key[0], key[1], key[2], self.weightedAverage(data)))
        sorted_ans = sorted(ans, key=lambda x: x[3])
        return sorted_ans
    
    def weightedAverage(self, data):
        odds_times_weight = 0
        sum_of_weights = 0
        for odds, book in data:
            if book in self.book_to_weight:
                odds_times_weight += odds*self.book_to_weight[book]
                sum_of_weights += self.book_to_weight[book]
            else:
                odds_times_weight += odds
                sum_of_weights += 1
            if book not in self.book_to_weight and book not in self.private_books:
                print("Book not in BookWeight: "+book)
        return round(odds_times_weight/sum_of_weights)
    
    def sieve(self, category, map):
        ans = []
        hold = set()
        for x in self.prizepicks_data: # (name, type, line, date)
            name, type, line = x[0], x[1], x[2]
            if type == category:
                hold.add((name, line-0.5, "whole"))
                hold.add((name, line, "half"))
                hold.add((name, line+0.5, "whole"))
        for name, type, line, odds in map:
            if (name, line, "half") in hold and odds > -140 and odds < 140:
                ans.append((name, type, line, odds, "half"))
        return ans
        
    def getData(self):
        for category in self.categories:
            if category in {"Points", "Rebounds", "Assists", "3-PT Made", "Blocked Shots", "Steals", "Pts+Rebs+Asts", "Pts+Rebs", "Pts+Asts", "Rebs+Asts"}:
                print("-------------------"+category+"-------------------")
                print(self.getCategory(category))
