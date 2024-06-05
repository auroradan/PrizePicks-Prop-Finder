class BookWeight:
    def __init__(self):
        self.book_to_weight = {"FanDuel":34.04, "Caesars":7.67, "BetMGM":12.37, "DraftKings":17.18, "BetRivers":2.01}
        self.private_books = set(["MyBookie.ag", "BetOnline.ag", "Bovada"])
    
    def getBookToWeight(self):
        return self.book_to_weight
    
    def getPrivateBooks(self):
        return self.private_books