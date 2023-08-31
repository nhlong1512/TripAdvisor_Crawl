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
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import re

csv_file_path = 'D:/NPVSCode/CrawlData/TripAdvisor_Crawl/data/Food/Links/LinkPageProvinces.csv'
df = pd.read_csv(csv_file_path)
links_column = df['Link']
links_list = links_column.to_numpy()
print('Link__LISTSSSSSSSSSSSSSSSSSS',links_list)
print(links_column)


profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
url_file_driver = os.path.join('etc', 'geckodriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver, firefox_profile=profile)
driver = webdriver.Firefox(service=service)
# Create lists to store data
data_list = []

i = 0
numberLinkFood = -1
numberLinkFoodList = []
totalFood = 0
for link in links_list: 
    driver.get(link)
    sleep(random.randint(2,3))
    i += 1
    try:
        if link == 'https://www.tripadvisor.com.vn/Restaurants-g469418-Phu_Quoc_Island_Kien_Giang_Province.html':
            numberLinkFood == 11
            numberLinkFoodList.append(numberLinkFood)
            print('\nNUMBER_LINK_FOOD ------> {}'.format(i), numberLinkFood)
        numberLinkFood = driver.find_element("xpath", "/html/body/div[1]/main/div/div[4]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/span/span").text
        numberLinkFoodList.append(numberLinkFood)
        print('\nNUMBER_LINK_FOOD ------> {}'.format(i), numberLinkFood)
    except NoSuchElementException: 
        try: 
            numberLinkFood = driver.find_element("xpath", "/html/body/div[1]/main/div/div[3]/div[5]/div/div/span/span").text
            numberLinkFoodList.append(numberLinkFood)
            print('\nNUMBER_LINK_FOOD ------> {}'.format(i), numberLinkFood)
        except NoSuchElementException: 
            try: 
                numberLinkFood = driver.find_element("xpath", "/html/body/div[1]/main/div/div[3]/div[2]/div/div/span/span").text
                print('\nNUMBER_LINK_FOOD ------> {}'.format(i), numberLinkFood)
            except NoSuchElementException:
                try: 
                    numberLinkFood = driver.find_element("xpath", "/html/body/div[1]/main/div/div[4]/div/div/div/div[2]/div[1]/div[1]/div/div/span/span").text
                    numberLinkFoodList.append(numberLinkFood)
                    print('\nNUMBER_LINK_FOOD ------> {}'.format(i), numberLinkFood)
                except NoSuchElementException:
                    try: 
                        if link == 'https://www.tripadvisor.com.vn/Restaurants-g469418-Phu_Quoc_Island_Kien_Giang_Province.html':
                            numberLinkFood == 11
                            numberLinkFoodList.append(numberLinkFood)
                            print('\nNUMBER_LINK_FOOD ------> {}'.format(i), numberLinkFood)
                        else: 
                            numberLinkFood = -1
                            numberLinkFoodList.append(numberLinkFood)
                            print('\nNUMBER_LINK_FOOD ------> {}'.format(i) + " KienGiangPhuQuoc")
                    except NoSuchElementException:
                        print('NoSuchElementException')
                        numberLinkFood = -1
                        numberLinkFoodList.append(numberLinkFood)
                        pass
    except Exception as e:
        print('Exception: ', e)
        numberLinkFood = -1
        numberLinkFoodList.append(numberLinkFood)
        pass
    df2 = pd.DataFrame(numberLinkFoodList)
    df2.to_csv('../data/Food/Links/NumberFoodsProvince.csv', encoding='utf-8', index=False)
    
df2 = pd.DataFrame(numberLinkFoodList)
df2.to_csv('../data/Food/Links/NumberFoodsProvince.csv', encoding='utf-8', index=False)

print("/n Sum Food Links -----> ", sum(numberLinkFoodList))