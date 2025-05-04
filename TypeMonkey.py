# Web Scraping

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Keyboard Stuff
import keyboard
import pyautogui
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://monkeytype.com/")

def typer():
    time.sleep(1)
    for i in range(16):
        cur_page = driver.page_source
        code = BeautifulSoup(cur_page,"html.parser")
        words = code.find_all(class_ = "word")
        to_type = ""

        for i in words[-100:]:
            letters = i.find_all("letter")

            for j in letters:
                to_type += j.get_text()
            to_type += " "

        pyautogui.write(to_type)

while True:
    keyboard.wait("ctrl+a")
    typer()