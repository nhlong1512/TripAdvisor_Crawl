from ctypes.wintypes import SERVICE_STATUS_HANDLE
import numpy as np
from selenium import webdriver
from time import sleep
import random
import os
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import pandas as pd

#Declare browsers
url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://www.tripadvisor.com/Hotels-g293921-Vietnam-Hotels.html")
sleep(random.randint(10,15))
print("Click see all")    
see_all_btn = driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[12]/div/button")
see_all_btn.click()
elems = driver.find_elements(By.CSS_SELECTOR, ".jsTLT [href]")
links = [elem.get_attribute('href') for elem in elems]
titles = [elem_title.text for elem_title in elems] 
print('Titles --> ', titles)
print('Links --> ', links)

for i in range(1,3): 
    print("Crawl Page ", i+1, ": ")
    url_page = 'https://www.tripadvisor.com/Hotels-g293921-oa' + str(i*30) + '-Vietnam-Hotels.html'
    print(url_page)
    driver.get(url_page)
    sleep(random.randint(10,15))
    try:
        print("Click see all")    
        see_all_btn = driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[12]/div/button")
        see_all_btn.click()
    except ElementClickInterceptedException:
        print("ElementClickInterceptedException") 
        continue
    elems = driver.find_elements(By.CSS_SELECTOR, ".jsTLT [href]")
    links = [elem.get_attribute('href') for elem in elems]
    titles = [elem_title.text for elem_title in elems] 
    print('Titles page --> ', titles)
    print('Links --> ', links)
    
