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
        for name, type, line in self.prizepicks_data:
            temp.add(type)
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
        match category.lower():
            case "points":
                return self.sieve("points", self.getPropsAverage(self.points_map))
            case "rebounds":
                return self.sieve("rebounds", self.getPropsAverage(self.rebounds_map))
            case "assists":
                return self.sieve("assists", self.getPropsAverage(self.assists_map))
            case "threes":
                return self.sieve("threes", self.getPropsAverage(self.threes_map))
            case "blocks":
                return self.sieve("blocks", self.getPropsAverage(self.blocks_map))
            case "steals":
                return self.sieve("steals", self.getPropsAverage(self.steals_map))
            case "pra":
                return self.sieve("pra", self.getPropsAverage(self.pra_map))
            case "pr":
                return self.sieve("pr", self.getPropsAverage(self.pr_map))
            case "pa":
                return self.sieve("pa", self.getPropsAverage(self.pa_map))
            case "ra":
                return self.sieve("ra", self.getPropsAverage(self.ra_map))
            case _:
                print("invalid category")
    
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
        for name, type, line in self.prizepicks_data:
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
            print("-------------------"+category+"-------------------")
            print(self.getCategory(category))
