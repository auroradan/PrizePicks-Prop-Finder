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

class PRIZEPICKS_NFL_SCRAPER():
    def __init__(self):
        self.directory = '\\projections.json'
        self.lines = []
        self.getJSON()
        self.load()

    def getJSON(self):
        url = "https://api.prizepicks.com/projections?league_id=9"
        driver = webdriver.Firefox()
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "json-tab")))
        save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.save")))
        save_button.click()
        time.sleep(.5)
        p.press("enter")
        time.sleep(.5)
        p.press("left")
        time.sleep(.5)
        p.press("enter")
        time.sleep(2)
        driver.quit()

    def load(self):
        seive = {"passing", "receiving"}
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
                stat_type = self.statType(projection["attributes"]["stat_type"].lower()).lower()
                
                print(stat_type)
                score = flash_sale if flash_sale is not None else line_score
                if stat_type in seive:
                    player_projections.append((player_name, stat_type, score))
        self.lines = player_projections
        
    def statType(self, stat):
        if stat == "receiving yards":
            return "receiving"
        elif stat == "pass yards":
            return "passing"
        else:
            return stat
