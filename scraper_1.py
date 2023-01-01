# Import library and packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Slow down the script with time.sleep() 
import time
from time import sleep

# Import extensions to read and write to excel files
import pandas as pd
from openpyxl import load_workbook 
import openpyxl
import csv

# Step 1: Login to LinkedIn

# 1. Open Chrome and login to LinkedIn

# a. Initializing webdriver to connect Selenium to the web
driver = webdriver.Chrome()
url = 'https://www.linkedin.com/login'
driver.get(url)
sleep(2)

# get credentials from a safe file
credential = open('login_credential.txt')
line = credential.readlines()
username = line[0]
password = line[1]
print("- Finished importing login credentials")

# b. locate fields (login, password, sign in)

email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(username)
sleep(14)

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(password)
sleep(7)

login_field = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_field.click()
sleep(20)

# Step 2: Search for the profile we want to scrape

# a. Locate the search bar element
search_field = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')

# b. Find a desired row on excel, input the search query to the search bar
def GetURL():
  wb = openpyxl.load_workbook('selenium-tester.xlsx')
  sheet = wb['Sheet1']
  list(sheet.columns)[4]
  for row, cellObj in enumerate(list(sheet.columns)[4]):
    if row != 0:
      search_field.send_keys(cellObj.value)
      sleep(5)
      search_field.send_keys(Keys.RETURN)
      print(' - Finish searching ...')
      sleep(3)

# Step 3. Scrape the url
      try:
        profile_btn = driver.find_element(By.CLASS_NAME, "search-nec__hero-kcard-v2")
        if profile_btn:
          profile_btn.click()
        sleep(3)
        get_url = driver.current_url
        sleep(5)
        with open('output.csv', 'a',  newline = '') as file_output:
          writer = csv.writer(file_output, lineterminator='\n')
          writer.writerow({get_url})
      except:
        search_field.clear();
        sleep(5)
        with open('output.csv', 'a',  newline = '') as file_output:
          writer = csv.writer(file_output, lineterminator='\n')
          writer.writerow({"not found"})
      print(' - Your url ')
      print(str(get_url))
  return(get_url)
print(' - Print function')
print(GetURL())
