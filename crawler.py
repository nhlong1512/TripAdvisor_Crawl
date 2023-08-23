from ctypes.wintypes import SERVICE_STATUS_HANDLE
import numpy as np
from selenium import webdriver
from time import sleep
import random
import os
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import pandas as pd

#Declare browsers
url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://www.tripadvisor.com.vn/Hotels-g293921-Vietnam-Hotels.html")
sleep(random.randint(10,15))
try: 
    see_all_btn = driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[12]/div/button")
    see_all_btn.click()
except NoSuchElementException:
    try:
        sleep(random.randint(10,15))
        see_all_btn = driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[12]/div/button")
        see_all_btn.click()
    except NoSuchElementException:
        print("No hope to click see all button")
        pass
    pass
elems = driver.find_elements(By.CSS_SELECTOR, ".jsTLT [href]")
links = [elem.get_attribute('href') for elem in elems]
titles = [elem_title.text for elem_title in elems] 

# Create lists to store data
data_list = []


for link in links:
    title = -1
    price = -1
    rating = -1
    address = -1
    img_url = -1
    description = -1
    
    driver.get(link)
    elem = driver.find_element(By.CSS_SELECTOR, ".jvqAy")
    title = driver.find_element(By.CSS_SELECTOR, ".jvqAy").text
    rating = driver.find_element(By.CSS_SELECTOR, ".uwJeR").text
    #Image url
    img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div/div/div/div/div[1]/div/div[1]/div/ul/li[1]/div/div/picture/source[1]").get_attribute("srcset")
    
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
        print("Address --> ", address)
    except:
        try: 
            address = driver.find_element(By.CSS_SELECTOR, ".fHvkI").text
        except: 
            pass
        pass
    
    #Description
    try: 
        description = driver.find_element(By.CSS_SELECTOR, ".fIrGe").text
    except: 
        try: 
            description = driver.find_element(By.CSS_SELECTOR, ".QewHA").text
        except:
            try: 
                description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[9]/div/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[3]/div[1]/div[1]/span").text                                          
            except:
                pass
            pass    
        pass
        
    data_list.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Address": address,
        "Img_URL": img_url,
        "Description": description
    })

# Create DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Print the DataFrame
print(df)
df.to_csv('./data/crawlTripAdvisor4.csv', encoding='utf-8', index=False)

driver.close()
# driver.get(links[0])
# elem = driver.find_elements(By.CSS_SELECTOR, ".jvqAy")
# title = driver.find_element(By.CSS_SELECTOR, ".jvqAy").text
# price = driver.find_element(By.CSS_SELECTOR, ".JPNOn").text
# rating = driver.find_element(By.CSS_SELECTOR, ".uwJeR").text
# address = driver.find_element(By.CSS_SELECTOR, ".fHvkI").text

# img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div/div/div/div/div[1]/div/div[1]/div/ul/li[1]/div/div/picture/source[1]").get_attribute("srcset")
# print('Title --> ', title)
# print('Price --> ', price)
# print('Rating --> ', rating)
# print('Address --> ', address)
# print('Img_url --> ', img_url)
# try: 
#     description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[4]/div/div[1]/div[4]/div/div/div/div/div[2]/div[1]/div[8]/div/div[1]/div/p[1]").text
#     print("Description --> ", description)
# except NoSuchElementException: 
#     print("NoSuchElementException")


# for i in range(1,5): 
#     print("Crawl Page ", i+1, ": ")
#     url_page = 'https://www.tripadvisor.com.vn/Hotels-g293921-oa' + str(i*30) + '-Vietnam-Hotels.html'
#     print(url_page)
#     driver.get(url_page)
#     sleep(random.randint(10,15))
#     try:
#         print("Click see all")    
#         see_all_btn = driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[12]/div/button")
#         see_all_btn.click()
#     except ElementClickInterceptedException:
#         print("ElementClickInterceptedException") 
#         pass
#     elems = driver.find_elements(By.CSS_SELECTOR, ".jsTLT [href]")
#     links = [elem.get_attribute('href') for elem in elems]
#     titles = [elem_title.text for elem_title in elems] 
#     print('Titles page --> ', titles)
#     print('Links --> ', links)
    
