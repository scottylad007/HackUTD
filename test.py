from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time

chrome_path = r"/Users/scottlombard/Projects/lava/chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.youtube.com")

searchReq = "Shoes"
searchBar = driver.find_element(By.ID, "search")
searchBar.click()
searchBar.send_keys(searchReq)
searchBar.send_keys(u"\ue007")

result = 4
links = driver.find_elements(By.ID, "video-title")
for link in links:
    print(link.get_attribute("href"))

watch = links[result].get_attribute("href")
driver.get(watch)