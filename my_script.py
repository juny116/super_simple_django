# from worldometer import Worldometer
# w = Worldometer()
# all = w.metrics_with_labels()
# print(all)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.worldometers.info")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#c1"))
    )
    # print(element)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    temp = soup.select("#c1 > div.counter-heading > span.counter-number > span.rts-counter")
    # temp = soup.select("#c1 > div.counter-heading.collapsed.inactive-header > span.counter-number > span.rts-counter")
    # print(temp)
    for s in temp:
        print(s.text)

finally:
    driver.quit()


# import requests
# import time
# url = "https://www.worldometers.info"
# s = requests.Session()
# r = s.get(url)
# # r = requests.get(url)
# time.sleep(1)
# r = s.get(url)

# temp = soup.select("#c1")
# print(temp)
# temp = soup.select("#c1 > div.counter-heading")
# print(temp)
# for s in temp:
#     print(s.select_one("span").text)

