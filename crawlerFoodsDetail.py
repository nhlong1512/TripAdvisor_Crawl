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


csv_file_path = 'D:/KLTN/TripAdvisor_Crawl/data/CrawlTripAdvisor_FoodLinks_All_1_SaiGon.csv'
df = pd.read_csv(csv_file_path)
links_column = df['link_food']
links_list = links_column.to_numpy()
print(links_list)


url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
driver = webdriver.Chrome(service=service)
# Create lists to store data
data_list = []


for link in links_list:
    print('URL_PAGE_IN_FUNCTION: -----> ', link)
    title = -1
    price = -1
    rating = -1
    address = -1
    img_url = -1
    description = -1
    rank_of_province = -1
    type_of_food = -1
    province = -1
    
    driver.get(link)
    try:
        title = driver.find_element(By.CSS_SELECTOR, ".HjBfq").text
    except Exception as e:
        pass
    
    try:
        rating = driver.find_element(By.CSS_SELECTOR, ".ZDEqb").text
    except Exception as e:
        pass
    #Image url
    try:
        img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div[3]/div/div/img").get_attribute("src")
    except Exception as e:
        pass
    
    #Price
    try: 
        price = driver.find_element(By.CSS_SELECTOR, ".SrqKb").text
    except Exception as e: 
        pass
    
    #Address
    try: 
        address = driver.find_element(By.CSS_SELECTOR, ".yEWoV").text
    except Exception as e:
        pass
    
    #Description
    try: 
        description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[6]/div/div[1]/div[3]/div/div[5]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/p").text
    except Exception as e: 
        pass
    #Rank of province
    try: 
        rank_of_province = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[4]/div/div/div[2]/span[2]/a/span").text
    except Exception as e:
        pass
    
    #Type of food
    try: 
        type_of_food = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[4]/div/div/div[2]/span[3]").text
    except Exception as e:
        pass
    
        
    data_list.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Address": address,
        "Img_URL": img_url,
        "Description": description,
        "Rank_of_province": rank_of_province,
        "Type_of_food": type_of_food,
        "Province": "Thành phố Hồ Chí Minh"
    }) 
    df2 = pd.DataFrame(data_list)
    df2.to_csv('./data/CrawlTripAdvisor_Hotels_All_1.csv', encoding='utf-8', index=False)
