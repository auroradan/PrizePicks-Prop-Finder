from collections import defaultdict
from NHLPropFinder.ODDS_NHL_SCRAPER import ODDS_NHL_SCRAPER
from NHLPropFinder.PRIZEPICKS_NHL_SCRAPER import PRIZEPICKS_NHL_SCRAPER
from BookWeight import BookWeight


class NHLPropFinder():
    
    def __init__(self):
        self.nhl_data = ODDS_NHL_SCRAPER()
        self.prizepicks_data = PRIZEPICKS_NHL_SCRAPER().lines
        self.book_to_weight = BookWeight().getBookToWeight()
        self.private_books = BookWeight().getPrivateBooks()
        self.categories = []
        self.condense()
        self.getData()
        
    def condense(self):
        temp = set()
        for x in self.prizepicks_data:
            temp.add(x[1])
        self.categories = list(temp)
        self.saves_map = self.data_condenser(self.nhl_data.saves)
        self.shots_map = self.data_condenser(self.nhl_data.shots)
        self.points_map = self.data_condenser(self.nhl_data.points)
        self.blocks_map = self.data_condenser(self.nhl_data.blocks)
        self.assists_map = self.data_condenser(self.nhl_data.assists)

    def data_condenser(self, data):
        ans = defaultdict(list)
        for prop in data:
            key = (prop[0], prop[1], prop[2])
            ans[key].append((prop[3], prop[4]))
        return ans
    
    def getCategory(self, category):
        match category.lower():
            case "Goalie Saves":
                return self.sieve("Goalie Saves", self.getPropsAverage(self.saves_map))
            case "Shots On Goal":
                return self.sieve("Shots On Goal", self.getPropsAverage(self.shots_map))
            case "Blocked Shots":
                return self.sieve("Blocked Shots", self.getPropsAverage(self.blocks_map))
            case "Points":
                return self.sieve("Points", self.getPropsAverage(self.points_map))
            case "Assists":
                return self.sieve("Assists", self.getPropsAverage(self.assists_map))
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
            print("-------------------"+category+"-------------------")
            print(self.getCategory(category))
