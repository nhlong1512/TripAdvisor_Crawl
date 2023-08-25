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
1->209
"""

#Declare browsers
url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
driver = webdriver.Chrome(service=service)
# Create lists to store data
links_list = []


# def wait_and_click_see_all_btn():
#     max_attempts = 5  # Số lần thử tối đa
#     attempt = 0
    
#     while attempt < max_attempts:
#         try:
#             see_all_btn = driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[12]/div/button")
#             see_all_btn.click()
#             return  # Thoát khỏi vòng lặp nếu nhấp thành công
#         except NoSuchElementException:
#             print("See All button not found, attempt:", attempt + 1)
#         except ElementNotInteractableException:
#             print("Failed to click See All button, attempt:", attempt + 1)
#         except ElementClickInterceptedException:
#             print("Failed to click See All button, attempt:", attempt + 1)
            
#         attempt += 1
#         sleep(3)  # Đợi 3 giây trước khi thử lại


def crawl_one_page(url_page): 
    # Open URL
    print('URL_PAGE_IN_FUNCTION: -----> ', url_page)
    driver.get(url_page)
    sleep(random.randint(10,15))
    # wait_and_click_see_all_btn()
    elems = driver.find_elements(By.CSS_SELECTOR, ".biGQs [href]")
    links = [elem.get_attribute('href') for elem in elems]
    print(links)
    for link in links:
        links_list.append(link)
    df = pd.DataFrame(links_list)
    df.to_csv('./data/CrawlTripAdvisor_FoodLinks_All_1_SaiGon.csv', encoding='utf-8', index=False)


#Loop crawl pages
for page_index in range(0,209): 
    page_oa = page_index * 30
    urlPage = 'https://www.tripadvisor.com.vn/FindRestaurants?geo=293925&offset=' + str(page_oa) + '&broadened=true'
    print(urlPage)
    crawl_one_page(urlPage)   
     
df = pd.DataFrame(links_list)
df.to_csv('./data/CrawlTripAdvisor_FoodLinks_All_1_SaiGon.csv', encoding='utf-8', index=False)