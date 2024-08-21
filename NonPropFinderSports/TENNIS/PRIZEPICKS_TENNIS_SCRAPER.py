import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as p
import time
from Supplier import Supplier
from datetime import datetime, timezone, timedelta

class PRIZEPICKS_TENNIS_SCRAPER():
    def __init__(self):
        supplier = Supplier()
        self.directory = supplier.get_directory()
        self.lines = []
        self.getJSON()
        self.load()

    def getJSON(self):
        url = "https://api.prizepicks.com/projections?league_id=5"
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
                stat_type = projection["attributes"]["stat_type"]
                
                start_time = projection["attributes"]["start_time"]
                dt = datetime.fromisoformat(start_time)
                central_time = dt.astimezone(timezone(timedelta(hours=-5)))
                month = central_time.strftime("%b")
                day = central_time.strftime("%d").lstrip('0')
                formatted_date = central_time.strftime(f"{month}-{day}-%Y %I:%M %p")
                
                player_projections.append((player_name, stat_type, line_score, formatted_date))

        self.lines = player_projections