# PrizePicks Prop Finder

## Overview
PrizePicks is a Daily Fantasy Sports app that allows users to place sports bets on player props given a line where a player can go strictly over or under the line (ex: if a basketball player can get over or under 11 points in a game). PrizePicks Prop Finder uses Selenium to obtain player projection lines from the PrizePicks API and then utilizes The Odds API by making separate HTTP requests to access 20 different sportsbooks to retrieve player props with the highest odds on PrizePicks. The player prop with the highest probability of occurring can be chosen by using a weighted average the highest odds across all sportsbooks. The weighted average is based on a sportsbook's market cap.

### Supported Sports for PrizePicks
- NBA
- NFL
- NHL
- NCAAB
- MLB
- WNBA

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
pip install pandas xlsxwriter
pip install datetime
```

## Usage

### Running the code
Locate the supplier file and add the information accordingly. Example of a Supplier.py file filled out accordingly below.
```py
def __init__(self):
        # The key is the API key for the-odds-api at https://the-odds-api.com/#get-access
        self.key = "12345678987654321abcdefgefdcba"
        
        # The directory is the location of the projections.json file
        self.directory = "C:\\Users\\youraccountname\\Downloads\\projections.json"
```
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

Sample outcome produced in terminal
```
-------------------assists-------------------
[('Jeremy Sochan', 'Over', 3.5, -235), ('Karl-Anthony Towns', 'Over', 2.5, -233), ('Zion Williamson', 'Over', 3.5, -230), ('Tyler Herro', 'Over', 4.5, -210), ('Derrick White', 'Under', 6.5, -205), ('Malcolm Brogdon', 'Under', 7.5, -205), ('Bam Adebayo', 'Over', 4.5, -200), ('Anfernee Simons', 'Under', 5.5, -177), ('Nikola Jokic', 'Over', 8.5, -170), ('CJ McCollum', 'Over', 4.5, -169), ('Stephen Curry', 'Over', 4.5, -168), ('CJ McCollum', 'Under', 5.5, -164), ('Brandon Ingram', 'Over', 5.5, -163), ('Stephen Curry', 'Under', 5.5, -163), ('LeBron James', 'Under', 9.5, -159), ('Anfernee Simons', 'Over', 4.5, -158), ('Terry Rozier', 'Under', 7.5, -158), ('Brandon Ingram', 'Under', 6.5, -156), ('Bam Adebayo', 'Under', 5.5, -153), ('LeBron James', 'Over', 8.5, -149), ('Karl-Anthony Towns', 'Under', 3.5, -147), ('Terry Rozier', 'Over', 6.5, -147), ('Tyrese Haliburton', 'Over', 11.5, -145), ('Chris Paul', 'Over', 7.5, -144), ('Tyrese Haliburton', 'Under', 12.5, -140), ('Chris Paul', 'Under', 8.5, -138), ('Herbert Jones', 'Under', 2.5, -137), ('Zion Williamson', 'Under', 4.5, -137), ('Jeremy Sochan', 'Under', 4.5, -137), ('Derrick White', 'Over', 5.5, -136), ('Tyler Herro', 'Under', 5.5, -136), ('Scoot Henderson', 'Over', 4.5, -136), ('Malcolm Brogdon', 'Over', 6.5, -134), ('Coby White', 'Over', 5.5, -130), ('Nikola Jokic', 'Under', 9.5, -129), ('Devin Vassell', 'Under', 3.5, -126), ('DeMar DeRozan', 'Under', 6.5, -125), ('Jerami Grant', 'Under', 2.5, -122), ('Cade Cunningham', 'Under', 6.5, -121), ('Jamal Murray', 'Under', 6.5, -121), ('Jayson Tatum', 'Over', 4.5, -120), ('Ja Morant', 'Under', 7.5, -119), ('Jrue Holiday', 'Under', 5.5, -113), ('Ja Morant', 'Over', 7.5, -111), ('Jrue Holiday', 'Over', 5.5, -95), ('Jamal Murray', 'Over', 6.5, -90), ('Cade Cunningham', 'Over', 6.5, -89), ('Jerami Grant', 'Over', 2.5, -80), ('Devin Vassell', 'Over', 3.5, -55), ('Jayson Tatum', 'Under', 4.5, -43), ('Coby White', 'Under', 5.5, -15), ('DeMar DeRozan', 'Over', 6.5, -5), ('Nikola Jokic', 'Over', 9.5, 23), ('Malcolm Brogdon', 'Under', 6.5, 27), ('Derrick White', 'Under', 5.5, 59), ('Scoot Henderson', 'Under', 4.5, 70), ('Tyler Herro', 'Over', 5.5, 78), ('Herbert Jones', 'Over', 2.5, 104), ('Zion Williamson', 'Over', 4.5, 104), ('Jeremy Sochan', 'Over', 4.5, 104), ('Tyrese Haliburton', 'Over', 12.5, 105), ('Chris Paul', 'Over', 8.5, 108), ('Chris Paul', 'Under', 7.5, 109), ('Tyrese Haliburton', 'Under', 11.5, 110), ('Terry Rozier', 'Under', 6.5, 111), ('Karl-Anthony Towns', 'Over', 3.5, 112), ('LeBron James', 'Under', 8.5, 114), ('Bam Adebayo', 'Over', 5.5, 116), ('Brandon Ingram', 'Under', 5.5, 117), ('Brandon Ingram', 'Over', 6.5, 118), ('LeBron James', 'Over', 9.5, 118), ('Terry Rozier', 'Over', 7.5, 119), ('Anfernee Simons', 'Under', 4.5, 120), ('Stephen Curry', 'Over', 5.5, 122), ('CJ McCollum', 'Over', 5.5, 124), ('CJ McCollum', 'Under', 4.5, 125), ('Stephen Curry', 'Under', 4.5, 127), ('Anfernee Simons', 'Over', 5.5, 132), ('Derrick White', 'Over', 6.5, 142), ('Bam Adebayo', 'Under', 4.5, 148), ('Malcolm Brogdon', 'Over', 7.5, 150), ('Tyler Herro', 'Under', 4.5, 155), ('Karl-Anthony Towns', 'Under', 2.5, 160), ('Zion Williamson', 'Under', 3.5, 170), ('Jeremy Sochan', 'Under', 3.5, 170)]
-------------------points-------------------
[('Malcolm Brogdon', 'Under', 17.5, -157), ('Jeremy Sochan', 'Over', 11.5, -140), ('Nick Richards', 'Under', 10.5, -138), ('Klay Thompson', 'Over', 18.5, -133), ('Jerami Grant', 'Over', 20.5, -133), ('Toumani Camara', 'Under', 7.5, -132), ('Jabari Walker', 'Over', 7.5, -132), ('Anthony Davis', 'Over', 28.5, -132), ('Nick Richards', 'Over', 9.5, -132), ('Derrick White', 'Under', 18.5, -130), ('Chris Paul', 'Over', 7.5, -130), ('Jeremy Sochan', 'Under', 12.5, -130), ('Alex Caruso', 'Under', 12.5, -128), ('Patrick Williams', 'Under', 14.5, -128), ('Herbert Jones', 'Over', 8.5, -128), ('Michael Porter Jr.', 'Over', 17.5, -128), ('Toumani Camara', 'Over', 6.5, -128), ('Trey Murphy III', 'Over', 13.5, -126), ('Bam Adebayo', 'Over', 22.5, -126), ('Jonathan Kuminga', 'Over', 12.5, -126), ('Devin Vassell', 'Under', 20.5, -126), ('Jonas Valanciunas', 'Under', 15.5, -125), ('Dario Saric', 'Under', 9.5, -125), ('Jrue Holiday', 'Over', 15.5, -124), ('Klay Thompson', 'Under', 19.5, -124), ('Bojan Bogdanovic', 'Under', 18.5, -123), ('Andrew Wiggins', 'Under', 12.5, -123), ('Jayson Tatum', 'Over', 29.5, -122), ('Kristaps Porzingis', 'Under', 22.5, -122), ('Jamal Murray', 'Under', 24.5, -122), ('Anthony Davis', 'Under', 29.5, -122), ('Lauri Markkanen', 'Under', 24.5, -121), ('Tyler Herro', 'Over', 24.5, -121), ('Karl-Anthony Towns', 'Over', 21.5, -120), ('Brandon Ingram', 'Over', 23.5, -120), ('Nikola Jokic', 'Under', 27.5, -120), ('Malaki Branham', 'Under', 9.5, -120), ('Scoot Henderson', 'Over', 12.5, -120), ('Jerami Grant', 'Under', 21.5, -120), ('DeMar DeRozan', 'Over', 27.5, -119), ('Stephen Curry', 'Over', 27.5, -119), ('Jalen Duren', 'Under', 10.5, -118), ('Ayo Dosunmu', 'Under', 10.5, -118), ('Coby White', 'Under', 24.5, -118), ('Anfernee Simons', 'Over', 27.5, -118), ('Cade Cunningham', 'Under', 23.5, -116), ('CJ McCollum', 'Over', 17.5, -116), ('Zion Williamson', 'Under', 24.5, -116), ('Kentavious Caldwell-Pope', 'Under', 10.5, -116), ('Terry Rozier', 'Over', 24.5, -116), ('Andre Drummond', 'Under', 15.5, -115), ('Tyrese Haliburton', 'Over', 25.5, -115), ('Zion Williamson', 'Over', 24.5, -115), ('Kentavious Caldwell-Pope', 'Over', 10.5, -115), ('LeBron James', 'Over', 27.5, -115), ('Miles Bridges', 'Over', 21.5, -115), ('Miles Bridges', 'Under', 21.5, -115), ('Andre Drummond', 'Over', 15.5, -114), ('CJ McCollum', 'Under', 17.5, -114), ('Terry Rozier', 'Under', 24.5, -114), ('Cade Cunningham', 'Over', 23.5, -113), ('Jalen Duren', 'Over', 10.5, -112), ('Tyrese Haliburton', 'Under', 25.5, -112), ('Jerami Grant', 'Over', 21.5, -112), ('Ayo Dosunmu', 'Over', 10.5, -111), ('Stephen Curry', 'Under', 27.5, -111), ('Nikola Jokic', 'Over', 27.5, -110), ('Malaki Branham', 'Over', 9.5, -110), ('Kristaps Porzingis', 'Over', 22.5, -109), ('Lauri Markkanen', 'Over', 24.5, -109), ('Scoot Henderson', 'Under', 12.5, -109), ('Anthony Davis', 'Over', 29.5, -109), ('Bojan Bogdanovic', 'Over', 18.5, -107), ('Andrew Wiggins', 'Over', 12.5, -107), ('Klay Thompson', 'Over', 19.5, -107), ('Ja Morant', 'Under', 27.5, -94), ('Malcolm Brogdon', 'Over', 16.5, -93), ('Malcolm Brogdon', 'Under', 16.5, -93), ('Coby White', 'Over', 24.5, -92), ('Anfernee Simons', 'Under', 27.5, -88), ('DeMar DeRozan', 'Under', 27.5, -87), ('Jayson Tatum', 'Under', 29.5, -86), ('LeBron James', 'Under', 27.5, -86), ('Tyler Herro', 'Under', 24.5, -81), ('Ja Morant', 'Over', 27.5, -77), ('Jamal Murray', 'Over', 24.5, -69), ('Jonas Valanciunas', 'Over', 15.5, -66), ('Brandon Ingram', 'Under', 23.5, -64), ('Jrue Holiday', 'Under', 15.5, -61), ('Karl-Anthony Towns', 'Under', 21.5, -60), ('Michael Porter Jr.', 'Under', 17.5, -54), ('Bam Adebayo', 'Under', 22.5, -54), ('Anthony Davis', 'Under', 28.5, -50), ('Herbert Jones', 'Under', 8.5, -48), ('Devin Vassell', 'Over', 20.5, -30), ('Alex Caruso', 'Over', 12.5, -29), ('Patrick Williams', 'Over', 14.5, -23), ('Derrick White', 'Over', 18.5, -22), ('Trey Murphy III', 'Under', 13.5, -22), ('Chris Paul', 'Under', 7.5, -21), ('Jonathan Kuminga', 'Under', 12.5, -6), ('Toumani Camara', 'Under', 6.5, 0), ('Jabari Walker', 'Under', 7.5, 2), ('Dario Saric', 'Over', 9.5, 10), ('Jeremy Sochan', 'Over', 12.5, 14), ('Jerami Grant', 'Under', 20.5, 20), ('Klay Thompson', 'Under', 18.5, 28), ('Toumani Camara', 'Over', 7.5, 60), ('Nick Richards', 'Under', 9.5, 104), ('Nick Richards', 'Over', 10.5, 105), ('Jeremy Sochan', 'Under', 11.5, 106), ('Malcolm Brogdon', 'Over', 17.5, 114)]
-------------------blocks-------------------
[('Jrue Holiday', 'Over', 0.5, -140), ('Brandon Ingram', 'Under', 0.5, -131), ('CJ McCollum', 'Over', 0.5, -128), ('Lauri Markkanen', 'Over', 0.5, -127), ('LeBron James', 'Under', 0.5, -122), ('Jayson Tatum', 'Over', 0.5, -121), ('DeMar DeRozan', 'Over', 0.5, -121), ('Jayson Tatum', 'Under', 0.5, -116), ('DeMar DeRozan', 'Under', 0.5, -116), ('LeBron James', 'Over', 0.5, -110), ('CJ McCollum', 'Under', 0.5, -109), ('Lauri Markkanen', 'Under', 0.5, -108), ('Brandon Ingram', 'Over', 0.5, 17), ('Jrue Holiday', 'Under', 0.5, 100)]
-------------------steals-------------------
[('Kentavious Caldwell-Pope', 'Under', 1.5, -133), ('Jeremy Sochan', 'Over', 0.5, -131), ('Jabari Walker', 'Over', 0.5, -130), ('Matisse Thybulle', 'Under', 1.5, -130), ('Michael Porter Jr.', 'Over', 0.5, -129), ('Andre Drummond', 'Under', 1.5, -128), ('Scoot Henderson', 'Over', 0.5, -125), ('Bojan Bogdanovic', 'Over', 0.5, -122), ('Klay Thompson', 'Over', 0.5, -120), ('Jalen Duren', 'Over', 0.5, -117), ('Jalen Duren', 'Under', 0.5, -116), ('Jonathan Kuminga', 'Over', 0.5, -116), ('Jonathan Kuminga', 'Under', 0.5, -114), ('Klay Thompson', 'Under', 0.5, -112), ('Bojan Bogdanovic', 'Under', 0.5, -110), ('Scoot Henderson', 'Under', 0.5, -105), ('Andre Drummond', 'Over', 1.5, -65), ('Michael Porter Jr.', 'Under', 0.5, -36), ('Kentavious Caldwell-Pope', 'Over', 1.5, -35), ('Jeremy Sochan', 'Under', 0.5, -2), ('Matisse Thybulle', 'Over', 1.5, -2), ('Jabari Walker', 'Under', 0.5, 100)]
-------------------ra-------------------
[('Malcolm Brogdon', 'Under', 12.5, -145), ('Derrick White', 'Over', 9.5, -143), ('Brandon Ingram', 'Over', 10.5, -143), ('Derrick White', 'Under', 10.5, -142), ('CJ McCollum', 'Over', 8.5, -138), ('Jeremy Sochan', 'Under', 11.5, -138), ('Tyrese Haliburton', 'Over', 15.5, -137), ('Jalen Duren', 'Over', 11.5, -136), ('Lauri Markkanen', 'Under', 9.5, -136), ('Miles Bridges', 'Over', 9.5, -136), ('Brandon Ingram', 'Under', 11.5, -135), ('Malcolm Brogdon', 'Over', 11.5, -135), ('Scoot Henderson', 'Under', 8.5, -135), ('Kristaps Porzingis', 'Over', 9.5, -133), ('Andre Drummond', 'Over', 16.5, -132), ('Zion Williamson', 'Under', 11.5, -132), ('Jonas Valanciunas', 'Over', 12.5, -131), ('Coby White', 'Over', 10.5, -130), ('Cade Cunningham', 'Over', 10.5, -129), ('Terry Rozier', 'Over', 10.5, -129), ('Alex Caruso', 'Under', 7.5, -127), ('Coby White', 'Under', 11.5, -127), ('Anfernee Simons', 'Over', 8.5, -127), ('Jerami Grant', 'Under', 7.5, -127), ('Michael Porter Jr.', 'Under', 9.5, -126), ('Jabari Walker', 'Over', 7.5, -126), ('Jrue Holiday', 'Over', 11.5, -124), ('DeMar DeRozan', 'Under', 11.5, -124), ('Tyrese Haliburton', 'Under', 16.5, -124), ('Ja Morant', 'Under', 13.5, -123), ('Chris Paul', 'Over', 11.5, -123), ('Tyler Herro', 'Under', 10.5, -122), ('Nick Richards', 'Over', 10.5, -122), ('Bam Adebayo', 'Over', 15.5, -120), ('Brandin Podziemski', 'Under', 10.5, -120), ('Jeremy Sochan', 'Over', 10.5, -120), ('Jayson Tatum', 'Under', 13.5, -118), ('Nikola Jokic', 'Under', 22.5, -118), ('Karl-Anthony Towns', 'Over', 13.5, -117), ('Stephen Curry', 'Over', 9.5, -116), ('Devin Vassell', 'Over', 7.5, -116), ('Anthony Davis', 'Under', 16.5, -116), ('Anthony Davis', 'Over', 16.5, -115), ('Stephen Curry', 'Under', 9.5, -114), ('Devin Vassell', 'Under', 7.5, -114), ('Karl-Anthony Towns', 'Under', 13.5, -113), ('Jayson Tatum', 'Over', 13.5, -112), ('Nikola Jokic', 'Over', 22.5, -110), ('Brandin Podziemski', 'Over', 10.5, -110), ('Nick Richards', 'Under', 10.5, -110), ('Ja Morant', 'Over', 13.5, -108), ('Tyler Herro', 'Over', 10.5, -108), ('Jabari Walker', 'Under', 7.5, -106), ('Jeremy Sochan', 'Under', 10.5, -106), ('LeBron James', 'Under', 17.5, -79), ('Bam Adebayo', 'Under', 15.5, -71), ('LeBron James', 'Over', 17.5, -71), ('Chris Paul', 'Under', 11.5, -68), ('DeMar DeRozan', 'Over', 11.5, -67), ('Jrue Holiday', 'Under', 11.5, -66), ('Alex Caruso', 'Over', 7.5, -63), ('Coby White', 'Over', 11.5, -54), ('Jerami Grant', 'Over', 7.5, -54), ('Anfernee Simons', 'Under', 8.5, -23), ('Tyrese Haliburton', 'Over', 16.5, -5), ('Cade Cunningham', 'Under', 10.5, 19), ('Terry Rozier', 'Under', 10.5, 19), ('Michael Porter Jr.', 'Over', 9.5, 28), ('Andre Drummond', 'Under', 16.5, 33), ('Kristaps Porzingis', 'Under', 9.5, 35), ('Malcolm Brogdon', 'Under', 11.5, 37), ('Tyrese Haliburton', 'Under', 15.5, 38), ('Jonas Valanciunas', 'Under', 12.5, 49), ('CJ McCollum', 'Under', 8.5, 56), ('Zion Williamson', 'Over', 11.5, 60), ('Coby White', 'Under', 10.5, 102), ('Lauri Markkanen', 'Over', 9.5, 103), ('Jalen Duren', 'Under', 11.5, 104), ('Brandon Ingram', 'Over', 11.5, 104), ('Scoot Henderson', 'Over', 8.5, 104), ('Miles Bridges', 'Under', 9.5, 104), ('Jeremy Sochan', 'Over', 11.5, 106), ('Derrick White', 'Under', 9.5, 109), ('Brandon Ingram', 'Under', 10.5, 109), ('Derrick White', 'Over', 10.5, 110), ('Malcolm Brogdon', 'Over', 12.5, 110)]
-------------------rebounds-------------------
[('Stephen Curry', 'Over', 3.5, -220), ('Coby White', 'Over', 4.5, -200), ('Devin Vassell', 'Under', 4.5, -200), ('Malcolm Brogdon', 'Under', 5.5, -200), ('Miles Bridges', 'Under', 7.5, -200), ('Ja Morant', 'Under', 6.5, -195), ('Jrue Holiday', 'Under', 6.5, -190), ('Patrick Williams', 'Over', 4.5, -190), ('Alex Caruso', 'Under', 4.5, -186), ('Tyler Herro', 'Under', 5.5, -186), ('Kristaps Porzingis', 'Under', 8.5, -182), ('Brandon Ingram', 'Under', 5.5, -182), ('Michael Porter Jr.', 'Under', 8.5, -175), ('Cade Cunningham', 'Over', 3.5, -173), ('Derrick White', 'Under', 4.5, -172), ('Derrick White', 'Over', 3.5, -166), ('Tyrese Haliburton', 'Under', 4.5, -160), ('Tyrese Haliburton', 'Over', 3.5, -160), ('Toumani Camara', 'Under', 5.5, -160), ('Cade Cunningham', 'Under', 4.5, -158), ('Alex Caruso', 'Over', 3.5, -158), ('Devin Vassell', 'Over', 3.5, -158), ('Jalen Duren', 'Over', 9.5, -155), ('Tyler Herro', 'Over', 4.5, -155), ('Karl-Anthony Towns', 'Over', 9.5, -152), ('Malcolm Brogdon', 'Over', 4.5, -152), ('Lauri Markkanen', 'Over', 7.5, -151), ('Brandon Ingram', 'Over', 4.5, -146), ('Karl-Anthony Towns', 'Under', 10.5, -144), ('Jrue Holiday', 'Over', 5.5, -142), ('Dario Saric', 'Over', 4.5, -142), ('Nikola Jokic', 'Under', 13.5, -140), ('Jonathan Kuminga', 'Under', 4.5, -140), ('Toumani Camara', 'Over', 4.5, -140), ('Patrick Williams', 'Under', 5.5, -139), ('Jalen Duren', 'Under', 10.5, -138), ('Nikola Jokic', 'Over', 12.5, -138), ('Michael Porter Jr.', 'Over', 7.5, -136), ('Miles Bridges', 'Over', 6.5, -135), ('Coby White', 'Under', 5.5, -134), ('Ja Morant', 'Over', 5.5, -134), ('Scoot Henderson', 'Under', 3.5, -133), ('Andrew Wiggins', 'Over', 3.5, -132), ('Kristaps Porzingis', 'Over', 7.5, -131), ('Herbert Jones', 'Under', 3.5, -131), ('Anthony Davis', 'Under', 13.5, -129), ('Stephen Curry', 'Under', 4.5, -128), ('Jabari Walker', 'Over', 6.5, -128), ('Jayson Tatum', 'Over', 8.5, -124), ('Andre Drummond', 'Over', 15.5, -124), ('Trey Murphy III', 'Under', 3.5, -124), ('Zion Williamson', 'Over', 6.5, -124), ('Jerami Grant', 'Over', 4.5, -124), ('Klay Thompson', 'Over', 3.5, -123), ('DeMar DeRozan', 'Over', 4.5, -122), ('CJ McCollum', 'Over', 3.5, -122), ('Jeremy Sochan', 'Under', 6.5, -119), ('Anfernee Simons', 'Over', 3.5, -118), ('Terry Rozier', 'Over', 3.5, -118), ('Bam Adebayo', 'Under', 10.5, -117), ('LeBron James', 'Under', 8.5, -117), ('Nick Richards', 'Under', 9.5, -117), ('Jonas Valanciunas', 'Under', 10.5, -116), ('Jamal Murray', 'Under', 4.5, -116), ('Kentavious Caldwell-Pope', 'Over', 2.5, -116), ('Chris Paul', 'Over', 3.5, -115), ('Jonas Valanciunas', 'Over', 10.5, -114), ('Kentavious Caldwell-Pope', 'Under', 2.5, -114), ('Chris Paul', 'Under', 3.5, -114), ('Jamal Murray', 'Over', 4.5, -113), ('Bam Adebayo', 'Over', 10.5, -113), ('LeBron James', 'Over', 8.5, -113), ('Anfernee Simons', 'Under', 3.5, -112), ('Nick Richards', 'Over', 9.5, -112), ('Terry Rozier', 'Under', 3.5, -112), ('DeMar DeRozan', 'Under', 4.5, -108), ('Klay Thompson', 'Under', 3.5, -108), ('Jeremy Sochan', 'Over', 6.5, -86), ('CJ McCollum', 'Under', 3.5, -84), ('Zion Williamson', 'Under', 6.5, -84), ('Jerami Grant', 'Under', 4.5, -78), ('Andre Drummond', 'Under', 15.5, -77), ('Trey Murphy III', 'Over', 3.5, -77), ('Stephen Curry', 'Over', 4.5, -54), ('Jayson Tatum', 'Under', 8.5, -39), ('Jabari Walker', 'Under', 6.5, -2), ('Anthony Davis', 'Over', 13.5, 30), ('Kristaps Porzingis', 'Under', 7.5, 33), ('Andrew Wiggins', 'Under', 3.5, 34), ('Herbert Jones', 'Over', 3.5, 40), ('Michael Porter Jr.', 'Under', 7.5, 53), ('Miles Bridges', 'Under', 6.5, 53), ('Scoot Henderson', 'Over', 3.5, 68), ('Karl-Anthony Towns', 'Over', 10.5, 70), ('Nikola Jokic', 'Under', 12.5, 72), ('Coby White', 'Over', 5.5, 78), ('Ja Morant', 'Under', 5.5, 81), ('Patrick Williams', 'Over', 5.5, 82), ('Lauri Markkanen', 'Over', 8.5, 100), ('Jalen Duren', 'Over', 10.5, 105), ('Nikola Jokic', 'Over', 13.5, 105), ('Jrue Holiday', 'Under', 5.5, 107), ('Jonathan Kuminga', 'Over', 4.5, 107), ('Dario Saric', 'Under', 4.5, 108), ('Toumani Camara', 'Under', 4.5, 108), ('Brandon Ingram', 'Under', 4.5, 111), ('Lauri Markkanen', 'Under', 7.5, 113), ('Karl-Anthony Towns', 'Under', 9.5, 114), ('Tyrese Haliburton', 'Under', 3.5, 115), ('Malcolm Brogdon', 'Under', 4.5, 115), ('Tyler Herro', 'Under', 4.5, 117), ('Cade Cunningham', 'Over', 4.5, 119), ('Devin Vassell', 'Under', 3.5, 119), ('Alex Caruso', 'Under', 3.5, 120), ('Tyrese Haliburton', 'Over', 4.5, 122), ('Toumani Camara', 'Over', 5.5, 122), ('Derrick White', 'Under', 3.5, 125), ('Cade Cunningham', 'Under', 3.5, 128), ('Michael Porter Jr.', 'Over', 8.5, 128), ('Brandon Ingram', 'Over', 5.5, 130), ('Derrick White', 'Over', 4.5, 131), ('Kristaps Porzingis', 'Over', 8.5, 132), ('Alex Caruso', 'Over', 4.5, 134), ('Jrue Holiday', 'Over', 6.5, 135), ('Tyler Herro', 'Over', 5.5, 138), ('Ja Morant', 'Over', 6.5, 139), ('Devin Vassell', 'Over', 4.5, 148), ('Malcolm Brogdon', 'Over', 5.5, 148), ('Miles Bridges', 'Over', 7.5, 148), ('Stephen Curry', 'Under', 3.5, 160), ('DeMar DeRozan', 'Over', 5.5, 165)]
-------------------threes-------------------
[('Jonas Valanciunas', 'Under', 0.5, -132), ('Kentavious Caldwell-Pope', 'Over', 1.5, -130), ('Bojan Bogdanovic', 'Under', 2.5, -126), ('Patrick Williams', 'Under', 1.5, -126), ('Terry Rozier', 'Over', 2.5, -122), ('Karl-Anthony Towns', 'Under', 1.5, -120), ('Stephen Curry', 'Over', 4.5, -115), ('Stephen Curry', 'Under', 4.5, -114), ('Karl-Anthony Towns', 'Over', 1.5, -110), ('Terry Rozier', 'Under', 2.5, -108), ('Bojan Bogdanovic', 'Over', 2.5, -60), ('Patrick Williams', 'Over', 1.5, -16), ('Kentavious Caldwell-Pope', 'Under', 1.5, -16), ('Jonas Valanciunas', 'Over', 0.5, 19)]
-------------------pr-------------------
[('LeBron James', 'Over', 35.5, -138), ('Michael Porter Jr.', 'Over', 25.5, -134), ('Jrue Holiday', 'Over', 21.5, -130), ('Kristaps Porzingis', 'Under', 31.5, -128), ('Toumani Camara', 'Under', 12.5, -128), ('DeMar DeRozan', 'Over', 31.5, -127), ('Zion Williamson', 'Over', 30.5, -127), ('Jonathan Kuminga', 'Over', 16.5, -127), ('Anfernee Simons', 'Over', 30.5, -127), ('Jamal Murray', 'Under', 29.5, -126), ('Jeremy Sochan', 'Over', 18.5, -126), ('Tyler Herro', 'Over', 29.5, -125), ('Jabari Walker', 'Under', 15.5, -125), ('Cade Cunningham', 'Over', 27.5, -124), ('CJ McCollum', 'Over', 20.5, -124), ('Kentavious Caldwell-Pope', 'Over', 12.5, -124), ('Tyrese Haliburton', 'Over', 30.5, -123), ('Andrew Wiggins', 'Under', 16.5, -123), ('Scoot Henderson', 'Under', 16.5, -123), ('Jalen Duren', 'Over', 20.5, -122), ('Kristaps Porzingis', 'Under', 30.5, -122), ('Jonas Valanciunas', 'Over', 25.5, -122), ('Jerami Grant', 'Over', 25.5, -122), ('Karl-Anthony Towns', 'Over', 31.5, -121), ('Klay Thompson', 'Under', 22.5, -121), ('Ayo Dosunmu', 'Over', 13.5, -120), ('Patrick Williams', 'Over', 19.5, -120), ('Herbert Jones', 'Under', 12.5, -120), ('Anthony Davis', 'Over', 42.5, -120), ('DeMar DeRozan', 'Under', 32.5, -119), ('Brandon Ingram', 'Over', 28.5, -119), ('Nick Richards', 'Over', 19.5, -119), ('Bojan Bogdanovic', 'Over', 21.5, -118), ('Alex Caruso', 'Over', 16.5, -118), ('Ja Morant', 'Under', 33.5, -118), ('Nikola Jokic', 'Under', 40.5, -118), ('Devin Vassell', 'Under', 24.5, -118), ('Trey Murphy III', 'Over', 17.5, -117), ('Malaki Branham', 'Under', 12.5, -117), ('Malcolm Brogdon', 'Under', 21.5, -117), ('Miles Bridges', 'Over', 28.5, -117), ('Derrick White', 'Under', 22.5, -116), ('Jayson Tatum', 'Over', 38.5, -116), ('Andre Drummond', 'Under', 31.5, -116), ('Lauri Markkanen', 'Over', 32.5, -116), ('Bam Adebayo', 'Under', 33.5, -116), ('Chris Paul', 'Over', 11.5, -116), ('Dario Saric', 'Under', 14.5, -116), ('Stephen Curry', 'Under', 32.5, -116), ('Terry Rozier', 'Under', 28.5, -116), ('LeBron James', 'Over', 36.5, -116), ('Coby White', 'Over', 29.5, -115), ('Michael Porter Jr.', 'Over', 26.5, -115), ('Derrick White', 'Over', 22.5, -114), ('Jayson Tatum', 'Under', 38.5, -114), ('Andre Drummond', 'Over', 31.5, -114), ('Lauri Markkanen', 'Under', 32.5, -114), ('Bam Adebayo', 'Over', 33.5, -114), ('Chris Paul', 'Under', 11.5, -114), ('Dario Saric', 'Over', 14.5, -114), ('Terry Rozier', 'Over', 28.5, -114), ('Alex Caruso', 'Under', 16.5, -113), ('Trey Murphy III', 'Under', 17.5, -113), ('Malaki Branham', 'Over', 12.5, -113), ('Malcolm Brogdon', 'Over', 21.5, -113), ('Miles Bridges', 'Under', 28.5, -113), ('Bojan Bogdanovic', 'Under', 21.5, -112), ('Ja Morant', 'Over', 33.5, -112), ('Nikola Jokic', 'Over', 40.5, -112), ('Stephen Curry', 'Over', 32.5, -112), ('Devin Vassell', 'Over', 24.5, -112), ('LeBron James', 'Under', 36.5, -112), ('Coby White', 'Under', 29.5, -111), ('Karl-Anthony Towns', 'Under', 31.5, -111), ('Brandon Ingram', 'Under', 28.5, -111), ('Michael Porter Jr.', 'Under', 26.5, -111), ('Nick Richards', 'Under', 19.5, -111), ('Jalen Duren', 'Under', 20.5, -110), ('Ayo Dosunmu', 'Under', 13.5, -110), ('Patrick Williams', 'Under', 19.5, 
-110), ('Herbert Jones', 'Over', 12.5, -110), ('DeMar DeRozan', 'Over', 32.5, -109), ('CJ McCollum', 'Under', 20.5, -109), ('Klay Thompson', 'Over', 22.5, -109), ('Tyrese Haliburton', 'Under', 30.5, -108), ('Jonas Valanciunas', 'Under', 25.5, -108), ('Kentavious Caldwell-Pope', 'Under', 12.5, -108), ('Jerami Grant', 'Under', 25.5, -108), ('Scoot Henderson', 'Over', 16.5, -108), ('Andrew Wiggins', 'Over', 16.5, -107), ('Cade Cunningham', 'Under', 27.5, -106), ('DeMar DeRozan', 'Under', 31.5, -106), ('Jamal Murray', 'Over', 29.5, -106), ('Jabari Walker', 'Over', 15.5, -106), ('Anfernee Simons', 'Under', 30.5, -105), ('Kristaps Porzingis', 'Over', 30.5, -104), ('Jonathan Kuminga', 'Under', 16.5, -104), ('Anthony Davis', 'Under', 42.5, -44), ('Jeremy Sochan', 'Under', 18.5, -25), ('Tyler Herro', 'Under', 29.5, -6), ('Kristaps Porzingis', 'Over', 31.5, -4), ('Toumani Camara', 'Over', 12.5, -4), ('Zion Williamson', 'Under', 30.5, 29), ('Jrue Holiday', 'Under', 21.5, 32), ('Michael Porter Jr.', 'Under', 25.5, 35), ('LeBron James', 'Under', 35.5, 38)]     
-------------------pa-------------------
[('Ja Morant', 'Over', 34.5, -130), ('Chris Paul', 'Over', 15.5, -128), ('Nick Richards', 'Under', 11.5, -128), ('Trey Murphy III', 'Under', 15.5, -124), ('Kentavious Caldwell-Pope', 'Over', 12.5, -124), ('Dario Saric', 'Under', 11.5, -124), ('Ayo Dosunmu', 'Over', 12.5, -123), ('Herbert Jones', 'Under', 11.5, -123), ('Bam Adebayo', 'Under', 28.5, -123), ('Brandon Ingram', 'Over', 29.5, -122), ('Lauri Markkanen', 'Over', 25.5, -122), ('Jonathan Kuminga', 'Under', 14.5, -122), ('Devin Vassell', 'Over', 23.5, -122), ('Derrick White', 'Under', 24.5, -121), ('Jrue Holiday', 'Over', 21.5, -121), ('Alex Caruso', 'Over', 15.5, -121), ('Jerami Grant', 'Over', 23.5, -121), ('Malcolm Brogdon', 'Under', 23.5, -121), ('Bojan Bogdanovic', 'Under', 20.5, -120), ('Jonas Valanciunas', 'Over', 17.5, -120), ('Jamal Murray', 'Under', 31.5, -120), ('Andrew Wiggins', 'Under', 13.5, -120), ('Anfernee Simons', 'Over', 32.5, -120), ('Terry Rozier', 'Over', 31.5, -120), ('Zion Williamson', 'Over', 28.5, -119), ('Stephen Curry', 'Over', 32.5, -119), ('Tyler Herro', 'Over', 29.5, -119), ('Miles Bridges', 'Over', 24.5, -119), ('Jayson Tatum', 'Under', 34.5, -118), ('Coby White', 'Over', 30.5, -118), ('Karl-Anthony Towns', 'Under', 25.5, -118), ('Michael Porter Jr.', 'Over', 19.5, -118), ('Nikola Jokic', 'Over', 36.5, -118), ('Klay Thompson', 'Under', 20.5, -118), ('Malaki Branham', 'Over', 12.5, -118), ('Jeremy Sochan', 'Over', 16.5, -117), ('Jalen Duren', 'Over', 12.5, -116), ('Jalen Duren', 'Under', 12.5, -116), ('Tyrese Haliburton', 'Under', 38.5, -116), ('Scoot Henderson', 'Under', 17.5, -116), ('Anthony Davis', 'Under', 32.5, -116), ('Cade Cunningham', 'Over', 30.5, -115), ('Cade Cunningham', 'Under', 30.5, -115), ('Tyrese Haliburton', 'Over', 38.5, -115), ('CJ McCollum', 'Over', 22.5, -115), ('CJ McCollum', 'Under', 22.5, -115), ('LeBron James', 'Over', 36.5, -115), ('LeBron James', 'Under', 36.5, -115), ('Coby White', 'Under', 30.5, -114), ('Scoot Henderson', 'Over', 17.5, -114), ('Anthony Davis', 'Over', 32.5, -114), ('Michael Porter Jr.', 'Under', 19.5, -113), ('Klay Thompson', 'Over', 20.5, -113), ('Tyler Herro', 'Under', 29.5, -113), ('Jeremy Sochan', 'Under', 16.5, -113), ('Jayson Tatum', 'Over', 34.5, -112), ('Nikola Jokic', 'Under', 36.5, -112), ('Malaki Branham', 'Under', 12.5, -112), ('Bojan Bogdanovic', 'Over', 20.5, -111), ('Jonas Valanciunas', 'Under', 17.5, -111), ('Zion Williamson', 'Under', 28.5, -111), ('Jamal Murray', 'Over', 31.5, -111), ('Andrew Wiggins', 'Over', 13.5, -111), ('Stephen Curry', 'Under', 32.5, -111), ('Anfernee Simons', 'Under', 32.5, -111), ('Malcolm Brogdon', 'Over', 23.5, -111), ('Miles Bridges', 'Under', 24.5, -111), ('Derrick White', 'Over', 24.5, -110), ('Jrue Holiday', 'Under', 21.5, -109), ('Ayo Dosunmu', 'Under', 12.5, -109), ('Brandon Ingram', 'Under', 29.5, -109), ('Lauri Markkanen', 'Under', 25.5, -109), ('Jonathan Kuminga', 'Over', 14.5, -109), ('Jerami Grant', 'Under', 23.5, -109), ('Karl-Anthony Towns', 'Over', 25.5, -108), ('Herbert Jones', 'Over', 11.5, -108), ('Trey Murphy III', 'Over', 15.5, -108), ('Dario Saric', 'Over', 11.5, -108), ('Devin Vassell', 'Under', 23.5, -108), ('Bam Adebayo', 'Over', 28.5, -107), ('Terry Rozier', 'Under', 31.5, -60), ('Chris Paul', 'Under', 15.5, -54), ('Kentavious Caldwell-Pope', 'Under', 12.5, -41), ('Nick Richards', 'Over', 11.5, -37), ('Alex Caruso', 'Under', 15.5, -29), ('Ja Morant', 'Under', 34.5, 100)]
-------------------pra-------------------
[('CJ McCollum', 'Over', 25.5, -137), ('Kristaps Porzingis', 'Under', 33.5, -132), ('Klay Thompson', 'Over', 24.5, -132), ('Devin Vassell', 'Under', 28.5, -131), ('Ayo Dosunmu', 'Under', 16.5, -130), ('Brandon Ingram', 'Over', 34.5, -130), ('Dario Saric', 'Under', 16.5, -130), ('LeBron James', 'Over', 44.5, -129), ('Jonas Valanciunas', 'Under', 28.5, -128), ('Scoot Henderson', 'Over', 20.5, -128), ('Jonathan Kuminga', 'Over', 18.5, -126), ('Patrick Williams', 'Under', 21.5, -125), ('Jabari Walker', 'Under', 16.5, -125), ('Jalen Duren', 'Over', 22.5, -124), ('Tyrese Haliburton', 'Over', 42.5, -124), ('Tyler Herro', 'Over', 34.5, -124), ('Jerami Grant', 'Over', 28.5, -124), ('Trey Murphy III', 'Over', 18.5, -123), ('Ja Morant', 'Over', 40.5, -123), ('Derrick White', 'Under', 28.5, -122), ('Jeremy Sochan', 'Under', 23.5, -122), ('Malcolm Brogdon', 'Under', 28.5, -121), ('Nick Richards', 'Over', 20.5, -121), ('Jrue Holiday', 'Over', 27.5, -120), ('DeMar DeRozan', 'Under', 39.5, -120), ('Michael Porter Jr.', 'Over', 27.5, -120), ('Andrew Wiggins', 'Under', 17.5, -120), ('Bam Adebayo', 'Over', 38.5, -120), ('Coby White', 'Under', 36.5, -119), ('Lauri Markkanen', 'Over', 33.5, -119), ('Zion Williamson', 'Over', 35.5, -119), ('Jamal Murray', 'Over', 35.5, -119), ('Nikola Jokic', 'Over', 49.5, -119), ('Miles Bridges', 'Over', 31.5, -119), ('Jayson Tatum', 'Under', 43.5, -118), ('Andre Drummond', 'Over', 32.5, -118), ('Cade Cunningham', 'Under', 34.5, -117), ('Anthony Davis', 'Over', 45.5, -117), ('DeMar DeRozan', 'Over', 38.5, -116), ('Alex Caruso', 'Over', 19.5, -116), ('Karl-Anthony Towns', 'Under', 35.5, -116), ('Stephen Curry', 'Under', 37.5, -116), ('Terry Rozier', 'Over', 35.5, -116), ('Bojan Bogdanovic', 'Over', 23.5, -115), ('Bojan Bogdanovic', 'Under', 23.5, -115), ('Chris Paul', 'Over', 19.5, -115), ('Chris Paul', 'Under', 19.5, -115), ('Anfernee Simons', 'Over', 36.5, -115), ('Andre Drummond', 'Under', 32.5, -114), ('Karl-Anthony Towns', 'Over', 35.5, -114), ('Stephen Curry', 'Over', 37.5, -114), ('Anfernee Simons', 'Under', 36.5, -114), ('Terry Rozier', 'Under', 35.5, -114), ('Cade Cunningham', 'Over', 34.5, -113), ('DeMar DeRozan', 'Under', 38.5, -113), ('Anthony Davis', 'Under', 45.5, -113), ('Jayson Tatum', 'Over', 43.5, -112), ('Alex Caruso', 'Under', 19.5, -112), ('Jamal Murray', 'Under', 35.5, -112), ('Jrue Holiday', 'Under', 27.5, -111), ('Coby White', 'Over', 36.5, -111), ('Lauri Markkanen', 'Under', 33.5, -111), ('Zion Williamson', 'Under', 35.5, -111), ('Nikola Jokic', 'Under', 49.5, -111), ('Andrew Wiggins', 'Over', 17.5, -111), ('DeMar DeRozan', 'Over', 39.5, -110), ('Bam Adebayo', 'Under', 38.5, -110), ('Miles Bridges', 'Under', 31.5, -110), ('Nick Richards', 'Under', 20.5, -110), ('Trey Murphy III', 'Under', 18.5, -108), ('Tyler Herro', 'Under', 34.5, -108), ('Jabari Walker', 'Over', 16.5, -106), ('Jeremy Sochan', 'Over', 23.5, -84), ('Malcolm Brogdon', 'Over', 28.5, -84), ('Derrick White', 'Over', 28.5, -58), ('Jalen Duren', 'Under', 22.5, -58), ('Jonathan Kuminga', 'Under', 18.5, -56), ('Scoot Henderson', 'Under', 20.5, -53), ('Jerami Grant', 'Under', 28.5, -49), ('Michael Porter Jr.', 'Under', 27.5, -46), ('LeBron James', 'Under', 44.5, -36), ('Patrick Williams', 'Over', 21.5, -25), ('CJ McCollum', 'Under', 25.5, -18), ('Devin Vassell', 'Over', 28.5, -15), ('Tyrese Haliburton', 'Under', 42.5, -8), ('Kristaps Porzingis', 'Over', 33.5, 0), ('Klay Thompson', 'Under', 24.5, 0), ('Ja Morant', 'Under', 40.5, 13), ('Jonas Valanciunas', 'Over', 28.5, 17), ('Brandon Ingram', 'Under', 34.5, 31), ('Ayo Dosunmu', 'Over', 16.5, 48), ('Dario Saric', 'Over', 16.5, 49)]        
```
Update: Depending on the PropFinder, it will have the trait ("Whole") or ("Half"). This simply just means whether PrizePicks is offering a whole number of the line or a half number of the line (Whole = 4.0, 5.0 etc. and Half = 3.5, 4.5 etc.)

### ERRORS
- The method for obtaining PrizePicks data uses Selenium Webdriver because HTTPS requests do not work on their API since it is not meant to be accessed. So, it uses code that would operate similarly to how a human would download the JSON file.
- If you get a "Failed to retrieve data: 401" means that you have exceeded the number of uses on your OddsAPI token (the free version allows for 500 requests). So, you would need to either make a new OddsAPI account to get a new token or upgrade versions
