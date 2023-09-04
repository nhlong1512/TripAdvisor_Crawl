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


url_file_driver = os.path.join('etc', 'chromedriver.exe')

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
url_file_driver = os.path.join('etc', 'geckodriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver, firefox_profile=profile)
driver = webdriver.Firefox(service=service)
# Create lists to store data
data_list = []
links_list = []
elems =[]
def crawl_one_page(url_page): 
    # Open URL
    print('URL_PAGE_IN_FUNCTION: -----> ', url_page)
    driver.get(url_page)
    sleep(random.randint(10,15))
    try: 
        elems = driver.find_elements(By.CSS_SELECTOR, ".tnGGX [href]")
    except Exception as e:
        print('Exception: ', e)
        pass
    
    links = [elem.get_attribute('href') for elem in elems if "#REVIEWS" not in elem.get_attribute('href')]
    if links:
        for link in links: 
            links_list.append(link)
        df = pd.DataFrame(links_list, columns=['Link'])  # Tạo DataFrame với cột 'Link'
        csv_path = '../data/ThingToDo/Links/FoodTourAllLinks2.csv'
        df.to_csv(csv_path, encoding='utf-8', index=False)
        print(f"Data written to {csv_path}")
    else:
        print("No links found to write")
        
#Loop crawl pages
crawl_one_page("https://www.tripadvisor.com.vn/Attractions-g293921-Activities-c36-Vietnam.html")
for page_oa in range(1050,1380,30): 
    urlPage = 'https://www.tripadvisor.com.vn/Attractions-g293921-Activities-c36-oa' + str(page_oa) + '-Vietnam.html'
    crawl_one_page(urlPage)

df = pd.DataFrame(links_list, columns=['Link'])  # Tạo DataFrame với cột 'Link'
df.to_csv('../data/Food/Links/FoodTourAllLinks2.csv', encoding='utf-8', index=False)