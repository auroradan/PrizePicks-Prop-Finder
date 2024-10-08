import requests
import json
from Supplier import Supplier

class ODDS_NFL_SCRAPER:
    
    def __init__(self):
        supplier = Supplier()
        self.api_key = supplier.get_key()
        self.ids = self.gameIDs()
        self.passing = []
        self.receiving = []
        self.attd = []
        self.rushing = []
        for id in self.ids:
            self.passing.extend(self.OddsPassing(id))
            self.receiving.extend(self.OddsReceiving(id))
            self.attd.extend(self.OddsATTD(id))
            self.rushing.extend(self.OddsRushing(id))
        
    
    def gameIDs(self):
        url = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey="+self.api_key+"&regions=us&markets=h2h&oddsFormat=american"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return [game["id"] for game in data]
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

    def OddsPassing(self, id):
        url = f"https://api.the-odds-api.com/v4/sports/americanfootball_nfl/events/{id}/odds?apiKey={self.api_key}&regions=us&markets=player_pass_yds&oddsFormat=american"
        return self.fetch_odds(url, "player_pass_yds")

    def OddsReceiving(self, id):
        url = f"https://api.the-odds-api.com/v4/sports/americanfootball_nfl/events/{id}/odds?apiKey={self.api_key}&regions=us&markets=player_reception_yds&oddsFormat=american"
        return self.fetch_odds(url, "player_reception_yds")
    
    def OddsATTD(self, id):
        url = f"https://api.the-odds-api.com/v4/sports/americanfootball_nfl/events/{id}/odds?apiKey={self.api_key}&regions=us&markets=player_anytime_td&oddsFormat=american"
        return self.fetch_attd(url)
    
    def OddsRushing(self, id):
        url = f"https://api.the-odds-api.com/v4/sports/americanfootball_nfl/events/{id}/odds?apiKey={self.api_key}&regions=us&markets=player_rush_yds&oddsFormat=american"
        return self.fetch_odds(url, "player_rush_yds")

    def fetch_odds(self, url, market_key):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                props = []
                for bookmaker in data["bookmakers"]:
                    for market in bookmaker["markets"]:
                        if market["key"] == market_key:
                            for outcome in market["outcomes"]:
                                props.append((
                                    outcome["description"],
                                    outcome["name"],
                                    outcome["point"],
                                    outcome["price"],
                                    bookmaker["title"]
                                ))
                return props
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []
        
    def fetch_attd(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                props = []
                for bookmaker in data["bookmakers"]:
                    for market in bookmaker["markets"]:
                        if market["key"] == "player_anytime_td":
                            for outcome in market["outcomes"]:
                                props.append((
                                    outcome["description"],
                                    "Over",
                                    0.5,
                                    outcome["price"],
                                    bookmaker["title"]
                                ))
                return props
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []