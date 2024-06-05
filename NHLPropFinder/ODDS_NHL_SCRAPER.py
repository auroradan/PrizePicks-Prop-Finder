import requests
from Supplier import Supplier

class ODDS_NHL_SCRAPER:
    def __init__(self):
        supplier = Supplier()
        self.api_key = supplier.get_key()
        self.base_url = "https://api.the-odds-api.com/v4/sports/icehockey_nhl/events/"
        self.ids = self.gameIDs()
        self.shots = []
        self.saves = []
        self.points = []
        self.blocks = []
        self.assists = []
        self.collect_all_odds()


    def collect_all_odds(self):
        for id in self.ids:
            self.shots.extend(self.get_odds(id, "player_shots_on_goal"))
            self.saves.extend(self.get_odds(id, "player_total_saves"))
            self.points.extend(self.get_odds(id, "player_points"))
            self.blocks.extend(self.get_odds(id, "player_blocked_shots"))
            self.assists.extend(self.get_odds(id, "player_assists"))


    def gameIDs(self):
        url = f"{self.base_url}?apiKey={self.api_key}&regions=us&markets=h2h&oddsFormat=american"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return [game["id"] for game in response.json()]
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return []

    def get_odds(self, id, market_type):
        url = f"{self.base_url}{id}/odds?apiKey={self.api_key}&regions=us&markets={market_type}&oddsFormat=american"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                props = []
                for bookmaker in data["bookmakers"]:
                    for market in bookmaker["markets"]:
                        if market["key"] == market_type:
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
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return []