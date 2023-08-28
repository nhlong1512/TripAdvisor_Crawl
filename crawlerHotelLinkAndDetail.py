from ctypes.wintypes import SERVICE_STATUS_HANDLE
from telnetlib import EC
import numpy as np
from selenium import webdriver
from time import sleep
import random
import os
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

#Declare browsers
url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
driver = webdriver.Chrome(service=service)
# Create lists to store data
data_list = []
links_list = []

csv_file_path = 'D:/KLTN/TripAdvisor_Crawl/data/ThingToDo/Links/ThingToDoAllLinks.csv'
df = pd.read_csv(csv_file_path)
links_column = df['Link']
links_list = links_column.to_numpy()
print(links_list)



def crawl_one_page(url_page): 
    # Open URL
    print('URL_PAGE_IN_FUNCTION: -----> ', url_page)
    driver.get(url_page)
    sleep(random.randint(10,15))
    elems = driver.find_elements(By.CSS_SELECTOR, ".jsTLT [href]")
    links = [elem.get_attribute('href') for elem in elems]
    print(links)
    for link in links:
        links_list.append(link)
        
#Loop crawl pages
for page_index in range(0,100): 
    page_oa = page_index * 30
    print('pageOA --> ', page_oa)
    urlPage=''
    if(page_index == 0): urlPage = 'https://www.tripadvisor.com.vn/Hotels-g293921-Vietnam-Hotels.html'
    if(page_index != 0): urlPage = 'https://www.tripadvisor.com.vn/Hotels-g293921-oa' + str(page_oa) + '-Vietnam-Hotels.html'
    print(urlPage)
    crawl_one_page(urlPage)


print('LINK_LIST: ', links_list)
df = pd.DataFrame(links_list)
    
df.to_csv('./data/CrawlTripAdvisor_HotelLinks_All_1.csv', encoding='utf-8', index=False)


for link in links_list:
    print('URL_PAGE_IN_FUNCTION: -----> ', link)
    title = -1
    price = -1
    rating = -1
    address = -1
    img_url = -1
    description = -1
    rank_of_province = -1
    
    driver.get(link)
    try:
        title = driver.find_element(By.CSS_SELECTOR, ".jvqAy").text
    except Exception as e:
        pass
    
    try:
        rating = driver.find_element(By.CSS_SELECTOR, ".uwJeR").text
    except Exception as e:
        pass
    #Image url
    try:
        img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div/div/div/div/div[1]/div/div[1]/div/ul/li[1]/div/div/picture/source[1]").get_attribute("srcset")
    except Exception as e:
        pass
    
    #Price
    try: 
        price = driver.find_element(By.CSS_SELECTOR, ".JPNOn").text
    except NoSuchElementException:
        try:
            price = driver.find_element(By.CSS_SELECTOR, ".WXMFC").text
        except:
            pass
        pass
    except StaleElementReferenceException: 
        pass
    
    #Address
    try: 
        address = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[6]/div/div/div/div/div/div[4]/div[1]/div[2]/span[2]/span").text
    except NoSuchElementException:
        try: 
            address = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[2]/div/div[2]/div/div/div/span[2]/span").text
        except: 
            address = driver.find_element(By.CSS_SELECTOR, ".fHvkI").text
            pass
        pass
    except StaleElementReferenceException:
        try: 
            address = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[2]/div/div[2]/div/div/div/span[2]/span").text
        except: 
            address = driver.find_element(By.CSS_SELECTOR, ".fHvkI").text
            pass
        pass
    except ElementClickInterceptedException:
        try: 
            address = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[2]/div/div[2]/div/div/div/span[2]/span").text
        except: 
            address = driver.find_element(By.CSS_SELECTOR, ".fHvkI").text
            pass
        pass
    
    #Description
    try: 
        description = driver.find_element(By.CSS_SELECTOR, ".fIrGe").text
    except NoSuchElementException: 
        try: 
            description = driver.find_element(By.CSS_SELECTOR, ".QewHA").text
        except:
            try: 
                description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[9]/div/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[3]/div[1]/div[1]/span").text                                          
            except:
                pass
            pass    
        pass
    except StaleElementReferenceException: 
        try: 
            description = driver.find_element(By.CSS_SELECTOR, ".QewHA").text
        except:
            try: 
                description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[9]/div/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[3]/div[1]/div[1]/span").text                                          
            except:
                pass
            pass    
        pass
    #Rank of province
    try: 
        rank_of_province = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[1]/div[2]/div/a/span").text
    except NoSuchElementException:
        pass
        
        
    data_list.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Address": address,
        "Img_URL": img_url,
        "Description": description,
        "Rank_of_province": rank_of_province,
    }) 

df2 = pd.DataFrame(data_list)
df2.to_csv('./data/CrawlTripAdvisor_Hotels_All_1.csv', encoding='utf-8', index=False)
