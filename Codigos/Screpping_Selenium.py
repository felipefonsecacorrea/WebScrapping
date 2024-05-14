import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service() #Usado para instaciar o chrome webdriver
options = webdriver.ChromeOptions() #definir preferencias do chrome
driver = webdriver.Chrome(service=service, options=options )

url = "https://www.youtube.com/"
driver.get(url)

driver.find_element(By.TAG_NAME, value="input").send_keys("Caneta azul")
time.sleep(1)

driver.find_element(By.ID, value="search-icon-legacy").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT, value='Maneol Gomes - Caneta Azul').click()
time.sleep(7)
driver.find_element(By.CLASS_NAME, value="ytp-skip-ad-button").click()
time.sleep(60)