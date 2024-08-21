from collections import defaultdict
from statistics import mean
from NCAABPropFinder.ODDS_NCAAB_SCRAPER import ODDS_NCAAB_SCRAPER
from NCAABPropFinder.PRIZEPICKS_NCAAB_SCRAPER import PRIZEPICKS_NCAAB_SCRAPER
from BookWeight import BookWeight

# from DK_NBA_SCRAPER import DK_NBA_SCRAPER
'''
DK_NBA_SCRAPER depricated since odds-api takes odds
from DK and more, so no need to get odds from DK twice 
'''
class NCAABPropFinder():
    
    def __init__(self):
        self.nba_data = ODDS_NCAAB_SCRAPER()
        self.prizepicks_data = PRIZEPICKS_NCAAB_SCRAPER().lines
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
        self.pra_map = self.data_condenser(self.nba_data.pra)
        

    def data_condenser(self, data):
        ans = defaultdict(list)
        for prop in data:
            key = (prop[0], prop[1], prop[2])
            ans[key].append((prop[3], prop[4]))
        return ans
    
    def getCategory(self, category):
        match category.lower():
            case "Points":
                return self.sieve("Points", self.getPropsAverage(self.points_map))
            case "Rebounds":
                return self.sieve("Rebounds", self.getPropsAverage(self.rebounds_map))
            case "Assists":
                return self.sieve("Assists", self.getPropsAverage(self.assists_map))
            case "3-PT Made":
                return self.sieve("3-PT Made", self.getPropsAverage(self.threes_map))
            case "Pts+Rebs+Asts":
                return self.sieve("Pts+Rebs+Asts", self.getPropsAverage(self.pra_map))
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
            print("-------------------"+category+"-------------------")
            print(self.getCategory(category))
