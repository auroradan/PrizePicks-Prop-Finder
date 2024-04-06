import requests
from KeySupplier import KeySupplier
'''
Go to https://the-odds-api.com/#get-access and create an account to get an api_key. replace self.api_key with the key given
'''
class ODDS_MLB_SCRAPER:
    def __init__(self):
        key_supplier = KeySupplier()
        self.api_key = key_supplier.get_key()
        self.base_url = "https://api.the-odds-api.com/v4/sports/baseball_mlb/events/"
        self.ids = self.gameIDs()
        self.pitcher_strikeouts = []
        self.total_bases = []
        self.hits_allowed = []
        self.pitcher_outs = []
        self.batter_hits_runs_rbis = []
        self.collect_all_odds()


    def collect_all_odds(self):
        for id in self.ids:
            self.pitcher_strikeouts.extend(self.get_odds(id, "pitcher_strikeouts"))
            self.total_bases.extend(self.get_odds(id, "batter_total_bases"))
            self.hits_allowed.extend(self.get_odds(id, "pitcher_hits_allowed"))
            self.pitcher_outs.extend(self.get_odds(id, "pitcher_outs"))
            self.batter_hits_runs_rbis.extend(self.get_odds(id, "batter_hits_runs_rbis"))


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