import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as p
import time

'''
Change self.directory to the folder where typical downloads go to. end the directory in projections.json
'''

class PRIZEPICKS_NBA_SCRAPER():
    def __init__(self):
        self.directory = ''
        self.lines = []
        self.getJSON()
        self.load()

    def getJSON(self):
        url = "https://api.prizepicks.com/projections?league_id=7"
        driver = webdriver.Firefox()
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "json-tab")))
        save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.save")))
        save_button.click()
        time.sleep(2)
        p.press("enter")
        time.sleep(.5)
        p.press("left")
        time.sleep(.5)
        p.press("enter")
        time.sleep(2)
        driver.quit()

    def load(self):
        seive = {"points", "rebounds", "assists", "threes", "blocks", "steals", "pra", "pr", "pa", "ra"}
        with open(self.directory, 'r') as file:
            json_data = json.load(file)
        player_names = {elem["id"]: elem["attributes"]["name"]
                        for elem in json_data["included"]
                        if elem["type"] == "new_player"}
        player_projections = []
        for projection in json_data["data"]:
            if projection["type"] == "projection":
                player_id = projection["relationships"]["new_player"]["data"]["id"]
                player_name = player_names.get(player_id, "Unknown Player")

                flash_sale = projection["attributes"].get("flash_sale_line_score")
                line_score = projection["attributes"]["line_score"]
                stat_type = self.statType(projection["attributes"]["stat_type"]).lower()
                if stat_type in seive:
                    player_projections.append((player_name, stat_type, line_score))
                if stat_type in seive and flash_sale is not None:
                    player_projections.append((player_name, stat_type, flash_sale))
        self.lines = player_projections
        
    def statType(self, stat):
        match stat:
            case "Pts+Rebs+Asts":
                return "pra"
            case "Pts+Asts":
                return "pa"
            case "Pts+Rebs":
                return "pr"
            case "Rebs+Asts":
                return "ra"
            case "3-PT Made":
                return "threes"
            case "Blocked Shots":
                return "blocks"
            case _:
                return stat