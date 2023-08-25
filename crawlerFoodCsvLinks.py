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
"""

#Declare browsers
url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
driver = webdriver.Chrome(service=service)
# Create lists to store data
links_list = []

def crawl_one_page(url_page): 
    # Open URL
    print('URL_PAGE_IN_FUNCTION: -----> ', url_page)
    driver.get(url_page)
    sleep(random.randint(10,15))
    # wait_and_click_see_all_btn()
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, ".biGQs [href]")
        links = [elem.get_attribute('href') for elem in elems]
        print(links)
        for link in links:
            links_list.append(link)
        df = pd.DataFrame(links_list)
        df.to_csv('./data/Food/LaoCai/CrawlTripAdvisor_FoodLinks_All_1_LaoCai.csv', encoding='utf-8', index=False)
    except Exception as e:
        print('Exception: ', e)
        pass


#Loop crawl pages
for page_index in range(0,10): 
    page_oa = page_index * 30
    urlPage = 'https://www.tripadvisor.com.vn/FindRestaurants?geo=311304&offset=' + str(page_oa) + '&broadened=true'
    print(urlPage)
    crawl_one_page(urlPage)   
     
df = pd.DataFrame(links_list)
df.to_csv('./data/Food/LaoCai/CrawlTripAdvisor_FoodLinks_All_1_LaoCai.csv', encoding='utf-8', index=False)