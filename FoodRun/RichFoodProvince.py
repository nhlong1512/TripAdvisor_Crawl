from ctypes.wintypes import SERVICE_STATUS_HANDLE
import time
import numpy as np
from selenium import webdriver
from time import sleep
import random
import os
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


url_file_driver = os.path.join('etc', 'chromedriver.exe')

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
url_file_driver = os.path.join('etc', 'geckodriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver, firefox_profile=profile)
driver = webdriver.Firefox(service=service)

links_list = []
elems = []
links =[]

# print('URL_PAGE_IN_FUNCTION: -----> ', url_page)
driver.get("https://www.tripadvisor.com.vn/Restaurants-g293921-Vietnam.html#LOCATION_LIST")
sleep(random.randint(3,5))
try:
    elems = driver.find_elements(By.CSS_SELECTOR, ".geo_name [href]")
    # elems.append(elem)
    links = [elem.get_attribute('href') for elem in elems]
except Exception as e:
    print('Exception: ', e)
    pass
print(links)
df = pd.DataFrame(links)
df.to_csv('../data/Food/Links/LinkPageProvinces.csv', encoding='utf-8', index=False)


def crawl_one_page(url_page): 
    # Open URL
    print('URL_PAGE_IN_FUNCTION: -----> ', url_page)
    driver.get(url_page)
    sleep(random.randint(3,5))
    for i in range (1, 21): 
        try:
            elem = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/ul/li[{}]/a".format(i) )
            # elems.append(elem)
            links.append(elem.get_attribute('href'))
        except Exception as e:
            print('Exception: ', e)
            pass
    print(links)
    df = pd.DataFrame(links)
    df.to_csv('../data/Food/Links/LinkPageProvinces.csv', encoding='utf-8', index=False)
#Loop crawl pages
for page_index in range(1,14): 
    page_oa = page_index * 20
    urlPage = 'https://www.tripadvisor.com.vn/Restaurants-g293921-oa' + str(page_oa) + '-Vietnam.html#LOCATION_LIST'
    print(urlPage)
    crawl_one_page(urlPage)   

df = pd.DataFrame(links)
df.to_csv('../data/Food/Links/LinkPageProvinces.csv', encoding='utf-8', index=False)