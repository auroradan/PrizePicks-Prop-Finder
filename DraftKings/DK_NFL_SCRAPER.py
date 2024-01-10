import requests
'''
DK Receiving - https://sportsbook.draftkings.com//sites/US-SB/api/v5/eventgroups/88808/categories/1342
'''
class DK_NFL_SCRAPER():
    
    def __init__(self):
        self.receiving = []
        self.receiving = self.DKReceiving()
    
    def DKReceiving(self):
        url = "https://sportsbook.draftkings.com//sites/US-SB/api/v5/eventgroups/88808/categories/1342"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            props = []
            for category in data.get("eventGroup", {}).get("offerCategories", []):
                if category.get("name") == "Receiving Props":
                    for offer in category.get("offerSubcategoryDescriptors", [])[0].get("offerSubcategory", {}).get("offers", []):
                        for item in offer:
                            if "Receiving Yards" in item.get("label", ""):
                                player_name = item.get("label").split(" Receiving Yards")[0]
                                for outcome in item.get("outcomes", []):
                                    props.append((player_name, outcome.get('label'), outcome.get("line"), outcome.get('oddsAmerican')))
        else:
            print(f"Failed to retrieve data: {response.status_code}")
        props.sort(key=lambda x: x[0])
        return props