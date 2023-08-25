from ctypes.wintypes import SERVICE_STATUS_HANDLE
import numpy as np
from selenium import webdriver
from time import sleep
import random
import os
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


"""
url detail: biGQs
https://www.tripadvisor.com.vn/FindRestaurants?geo=293925&offset=0&broadened=true
https://www.tripadvisor.com.vn/FindRestaurants?geo=293925&offset=6240&broadened=true
1 -> 209 SaiGon
1 -> 146 HaNoi
1 -> 62 DaNang
1 -> 31 NhaTrang 293928
1 -> 21 LamDong 293922
1 -> 17 Hue 293926
1 -> 13 BinhThuan 298086
1 -> 9 HaiPhong 303944
1 -> 9 LaoCai 311304
1 -> 9 VungTau 303946
1 -> 16 PhuQuoc - KienGiang 1184679
1 -> 7 CanTho 303942
1 -> 10 NinhBinh 303945
1 -> 16 DuongTo - KienGiang 1184676
1 -> 4 QuangBinh 659924
1 -> 5 HaLong 293923
1 -> 10 NinhHai 12866457
1 -> 2 BuonMaThuot 670918
"""

#Declare browsers
url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
driver = webdriver.Chrome(service=service)
# Create lists to store data
links_list = []
elems = []
links =[]

# print('URL_PAGE_IN_FUNCTION: -----> ', url_page)
driver.get("https://www.tripadvisor.com.vn/Restaurants-g293921-oa20-Vietnam.html#LOCATION_LIST")
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
    df.to_csv('./data/Food/Links/LinkPageProvinces.csv', encoding='utf-8', index=False)
#Loop crawl pages
for page_index in range(2,14): 
    page_oa = page_index * 20
    urlPage = 'https://www.tripadvisor.com.vn/Restaurants-g293921-oa' + str(page_oa) + '-Vietnam.html#LOCATION_LIST'
    print(urlPage)
    crawl_one_page(urlPage)   

df = pd.DataFrame(links)
df.to_csv('./data/Food/Links/LinkPageProvinces.csv', encoding='utf-8', index=False)