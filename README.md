# PrizePicks Prop Finder

## Overview
It uses Selenium to obtain player projection lines from the PrizePicks API and then utilizes The Odds API by making separate HTTP requests to access 20 different sportsbooks to retrieve player props with the highest odds on PrizePicks. The player prop with the highest probability of occurring can be chosen by averaging the highest odds across all sportsbooks.

### Supported Sportsbooks from The Odds API
- FanDuel
- DraftKings
- BetMGM
- Caesars (William Hill)
- BetRivers
- PointsBet
- Bovada
- MyBookie.ag
- Unibet
- TwinSpires
- WynnBet
- LowVig.ag
- batPARX
- ESPN BET
- Fliff
- SI Sportsbook
- Tipico
- SuperBook
- Wind Creek (Betfred PA)

## Getting Started

### Clone the Repository

Assuming you have [Git](https://git-scm.com/) installed on your computer, open your terminal and run:

```bash
git clone https://github.com/auroradan/PrizePicks-Prop-Finder.git
```

### Install Dependencies

```bash
pip install json
pip install selenium
pip install pyautogui
pip install time
pip install collections
pip install statistics
pip install requests
```

## Usage

### Running the code
Locate the PropFinder.py file and run

Sample JSON of The Odds API
```json
{
  "id": "0a25fa87e6a970c44bd5770e4b54440f",
  "sport_key": "basketball_nba",
  "sport_title": "NBA",
  "commence_time": "2023-12-29T00:40:00Z",
  "home_team": "Boston Celtics",
  "away_team": "Detroit Pistons",
  "bookmakers": [
    {
      "key": "draftkings",
      "title": "DraftKings",
      "markets": [
        {
          "key": "player_points",
          "last_update": "2023-12-28T20:30:33Z",
          "outcomes": [
            {
              "name": "Over",
              "description": "Bojan Bogdanovic",
              "price": -140,
              "point": 17.5
            },
            {
              "name": "Under",
              "description": "Bojan Bogdanovic",
              "price": 110,
              "point": 17.5
            },
            {
              "name": "Over",
              "description": "Cade Cunningham",
              "price": -120,
              "point": 23.5
            },
            {
              "name": "Under",
              "description": "Cade Cunningham",
              "price": -110,
              "point": 23.5
            },
            {
              "name": "Over",
              "description": "Derrick White",
              "price": -105,
              "point": 18.5
            },
            {
              "name": "Under",
              "description": "Derrick White",
              "price": -125,
              "point": 18.5
            }
```

Sample JSON of PrizePicks API retrieving player data to attach to the projected line
```json
{
      "type": "new_player",
      "id": "53834",
      "attributes": {
        "combo": false,
        "display_name": "Stephen Curry",
        "image_url": "https://static.prizepicks.com/images/players/nba/Stephen_Curry_8ec91366-faea-4196-bbfd-b8fab7434795.webp",
        "league": "NBA",
        "league_id": 7,
        "market": "Golden State",
        "name": "Stephen Curry",
        "position": "G",
        "team": "GSW",
        "team_name": "Warriors"
      }
```

Sample JSON of PrizePicks API connecting player to a projected line
```json
{
      "type": "projection",
      "id": "1851994",
      "attributes": {
        "adjusted_odds": null,
        "board_time": "2023-12-01T19:30:00-05:00",
        "custom_image": null,
        "description": "DET/BOS",
        "end_time": null,
        "flash_sale_line_score": null,
        "game_id": "7acd91df-77d5-4d2f-b047-776f85ae40ef",
        "is_promo": false,
        "line_score": 5.5,
        "odds_type": "standard",
        "projection_type": "Single Stat",
        "rank": 5,
        "refundable": true,
        "start_time": "2023-12-28T19:30:00-05:00",
        "stat_type": "3-PT Made (Combo)",
        "status": "pre_game",
        "today": true,
        "tv_channel": null,
        "updated_at": "2023-12-28T15:03:32-05:00"
      }
```
