from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import subprocess
import os

#insert sleep statements before each input request ~3 seconds
#select function based on literal value
#email/login
#add google to search function
#delay response request
#clean interactions/prompts

#create logo
#Push to github
#Fix README.md

myFile = open("/Users/scottlombard/Library/Containers/Me.lavagui/Data/Documents/file.txt", "w+")
subprocess.call('open /Applications/lavagui.app', shell=True)

def scottPrint(text):
    myFile = open("/Users/scottlombard/Library/Containers/Me.lavagui/Data/Documents/file.txt", "a")
    print(text)
    text = text + "\n"
    myFile.write(text)
    myFile.close()

start = sr.Recognizer()
with sr.Microphone() as source:
    scottPrint('Say Something!')
    audio = start.listen(source)
    scottPrint('Done!')
    start = start.recognize_google(audio)

if start == "open lava":
    scottPrint("lava opening")
else:
    exit()

chrome_path = r"/Users/scottlombard/Projects/lava/chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.scottalombard.com")
#driver.maximize_window()

'''
Repitition -> Functions

def rec1(var):
    var = sr.Recognizer()
    with sr.Microphone() as source:
        audio = var.listen(source)

def rec2(var):
    var = var.recognize_google(audio)
    chromeCommand(var)
'''

def changeSite():
    verify = "No"

    while verify != "yes":
        siteName = sr.Recognizer()
        with sr.Microphone() as source:
            scottPrint('What site would you like to search?')
            audio = siteName.listen(source)
            siteName = siteName.recognize_google(audio)
            scottPrint("Is https://www." + siteName + ".com correct?")
        verify = sr.Recognizer()
        with sr.Microphone() as source:
            audio = verify.listen(source)
            verify = verify.recognize_google(audio)

    driver.get("https://www." + siteName + ".com")

def back():
    driver.back()

def pause():
    timeout = sr.Recognizer()
    with sr.Microphone() as source:
        scottPrint('How long would you like to pause?')
        audio = timeout.listen(source)
        timeout = timeout.recognize_google(audio)

    if timeout == "cancel":
        return None

    scottPrint("Pausing for " + timeout)
    parser = timeout.split()

    minute = 60
    hour = 3600

    if parser[1] == "seconds":
        time.sleep(int(parser[0]))
    elif parser[1] == "minute":
        time.sleep(minute)
    elif parser[1] == "minutes":
        time.sleep(int(parser[0])*minute)
    elif parser[1] == "hour":
        time.sleep(hour)
    elif parser[1] == "hours":
        time.sleep(int(parser[0])*hour)

def search():
    searchReq = sr.Recognizer()
    with sr.Microphone() as source:
        scottPrint('What would you like to search?')
        audio = searchReq.listen(source)
        searchReq = searchReq.recognize_google(audio)
        scottPrint('You said: ' + searchReq)

#add buttons are under class="ytp-ad-skip-button ytp-button"
# this works for youtube only

    searchBar = driver.find_element(By.ID, "search")
    searchBar.click()
    searchBar.send_keys(searchReq)
    searchBar.send_keys(u"\ue007")

    links = driver.find_elements(By.ID, "video-title")    #index all links on the page

    scottPrint("You have 10 seconds to decide which result you would like to watch!")
    time.sleep(10)

    result = sr.Recognizer()
    with sr.Microphone() as source:
        scottPrint('What number is your desired video on the page?')
        audio = result.listen(source)
        result = result.recognize_google(audio)
        scottPrint('You selected video number' + result)

    watch = links[int(result)-1].get_attribute("href")
    driver.get(watch)
    #end youtube block

#all google results are under class="LC20lb"

def chromeCommand(choice):
    if choice == "open lava":   #Launch the application
        scottPrint("lava opening")
    elif choice == "change website":    #Change to any website
        changeSite()
    elif choice == "back":      #Go back one page
        back()
    elif choice == "pause":     #suppress prompts for a specified duration
        pause()
    elif choice == "search":    #Supports Youtube and Google currently
        search()

#login()
#select()

if __name__ == "__main__":
    choice = ""

    while choice != "quit":
        scottPrint('Say Something!')
        choice = sr.Recognizer()
        with sr.Microphone() as source:
            audio = choice.listen(source)
            choice = choice.recognize_google(audio)
            scottPrint('You said: ' + choice)
            chromeCommand(choice)

    driver.quit()

