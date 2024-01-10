import requests
'''
Go to https://the-odds-api.com/#get-access and create an account to get an api_key. replace self.api_key with the key given
'''
class ODDS_NBA_SCRAPER:
    def __init__(self):
        self.api_key = ""
        self.base_url = "https://api.the-odds-api.com/v4/sports/basketball_nba/events/"
        self.ids = self.gameIDs()
        self.points = []
        self.rebounds = []
        self.assists = []
        self.threes = []
        self.pra = []
        self.pr = []
        self.pa = []
        self.ra = []
        self.blocks = []
        self.steals = []
        self.collect_all_odds()


    def collect_all_odds(self):
        for id in self.ids:
            self.points.extend(self.get_odds(id, "player_points"))
            self.rebounds.extend(self.get_odds(id, "player_rebounds"))
            self.assists.extend(self.get_odds(id, "player_assists"))
            self.threes.extend(self.get_odds(id, "player_threes"))
            self.pra.extend(self.get_odds(id, "player_points_rebounds_assists"))
            self.pr.extend(self.get_odds(id, "player_points_rebounds"))
            self.pa.extend(self.get_odds(id, "player_points_assists"))
            self.ra.extend(self.get_odds(id, "player_rebounds_assists"))
            self.blocks.extend(self.get_odds(id, "player_blocks"))
            self.steals.extend(self.get_odds(id, "player_steals"))
            

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
                                    outcome["price"]
                                ))
                return props
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return []