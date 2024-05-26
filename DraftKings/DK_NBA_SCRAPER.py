import requests
'''
DK Points - https://sportsbook.draftkings.com//sites/US-SB/api/v5/eventgroups/42648/categories/1215
DK Rebounds - https://sportsbook.draftkings.com//sites/US-SB/api/v5/eventgroups/42648/categories/1216
DK Assists - https://sportsbook.draftkings.com//sites/US-SB/api/v5/eventgroups/42648/categories/1217
DK Player 3s - https://sportsbook.draftkings.com//sites/US-SB/api/v5/eventgroups/42648/categories/1218
'''
class DK_NBA_SCRAPER():
    
    def __init__(self):
        self.points = self.fetch_data("1215", "Points")
        self.rebounds = self.fetch_data("1216", "Rebounds")
        self.assists = self.fetch_data("1217", "Assists")
        self.threes = self.fetch_data("1218", "Three Pointers Made")
    
    def fetch_data(self, category_id, stat_type):
        url = f"https://sportsbook.draftkings.com//sites/US-SB/api/v5/eventgroups/42648/categories/{category_id}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                props = []
                for category in data.get("eventGroup", {}).get("offerCategories", []):
                    if category.get("name") == f"Player {stat_type}":
                        for offer in category.get("offerSubcategoryDescriptors", [])[0].get("offerSubcategory", {}).get("offers", []):
                            for item in offer:
                                if stat_type in item.get("label", ""):
                                    player_name = item.get("label").split(f" {stat_type}")[0]
                                    for outcome in item.get("outcomes", []):
                                        props.append((player_name, outcome.get('label'), outcome.get("line"), outcome.get('oddsAmerican')))
                props = sorted(props, key=lambda x: self.transformOdds(x[3]))
                return props
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []
    
    def transformOdds(self, odds_str):
        if odds_str.startswith('-'):
            return float(odds_str)
        else:
            return float(odds_str[1:]) + 100
        

scraper = DK_NBA_SCRAPER()
print(scraper.points[:20])
print("------------------")
print(scraper.rebounds[:20])
print("------------------")
print(scraper.assists[:20])