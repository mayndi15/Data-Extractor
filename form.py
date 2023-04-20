import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


file = pd.read_excel("file.xlsx", sheet_name=None)

url = "https://docs.google.com/forms/d/e/1FAIpQLScOjgkpwVVlnl2cI26guDokHuuQ7zwdMapibc9xKP7wqEF9cw/viewform?vc=0&c=0&w=1&flr=0"
button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
name = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
age = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'

for index, row in file["Profile"].iterrows():

    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome.get(url)

    time.sleep(1)

    url_name = chrome.find_element(By.XPATH, name)
    url_age = chrome.find_element(By.XPATH, age)

    url_name.send_keys(row["name"])
    url_age.send_keys(row["age"])

    chrome.find_element(By.XPATH, button).click()

chrome.quit()