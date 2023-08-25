from ctypes.wintypes import SERVICE_STATUS_HANDLE
import numpy as np
from selenium import webdriver
from time import sleep
import random
import os
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

#Declare browsers
url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://www.tripadvisor.com.vn/Hotels-g293921-Vietnam-Hotels.html")
sleep(random.randint(10,15))
try: 
    # see_all_btn = driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[12]/div/button")
    see_all_btn = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".rmyCe"))
    )
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
        rank_of_province = -1
        
        driver.get(link)
        sleep(random.randint(1,3))
        try: 
            title = driver.find_element(By.CSS_SELECTOR, ".jvqAy").text
        except NoSuchElementException:
            pass
        try:
            rating = driver.find_element(By.CSS_SELECTOR, ".uwJeR").text
        except NoSuchElementException:
            pass
        #Image url
        try:
            img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div/div/div/div/div[1]/div/div[1]/div/ul/li[1]/div/div/picture/source[1]").get_attribute("srcset")
        except NoSuchElementException:
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
            
        print("Address ---> ", address)    
        data_list.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Address": address,
            "Img_URL": img_url,
            "Description": description,
            "Rank_of_province": rank_of_province,
        }) 
        

# for page_index in range(30, 991, 30): 
#     if(page_index != 0): urlPage = 'https://www.tripadvisor.com.vn/Hotels-g293921-oa{}-Vietnam-Hotels.html'.format(page_index)
#     print(urlPage)
#     # driver.get(urlPage)
#     driver.get("https://www.tripadvisor.com.vn/Hotels-g293921-oa{}-Vietnam-Hotels.html".format(page_index))
#     sleep(random.randint(10,15))
#     try: 
#         see_all_btn = driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[12]/div/button")
#         see_all_btn.click()
#     except NoSuchElementException:
#         try:
#             sleep(random.randint(10,15))
#             see_all_btn = driver.find_element("xpath", "/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[12]/div/button")
#             see_all_btn.click()
#         except NoSuchElementException:
#             print("No hope to click see all button")
#             pass
#         pass
#     elems = driver.find_elements(By.CSS_SELECTOR, ".jsTLT [href]")
#     links = [elem.get_attribute('href') for elem in elems]
#     titles = [elem_title.text for elem_title in elems] 

#     # Create lists to store data
#     data_list = []


#     for link in links:
#             title = -1
#             price = -1
#             rating = -1
#             address = -1
#             img_url = -1
#             description = -1
#             rank_of_province = -1
            
#             driver.get(link)
#             sleep(random.randint(1,3))
#             try: 
#                 title = driver.find_element(By.CSS_SELECTOR, ".jvqAy").text
#             except NoSuchElementException:
#                 pass
#             try:
#                 rating = driver.find_element(By.CSS_SELECTOR, ".uwJeR").text
#             except NoSuchElementException:
#                 pass
#             #Image url
#             try:
#                 img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/div/div/div/div/div[1]/div/div[1]/div/ul/li[1]/div/div/picture/source[1]").get_attribute("srcset")
#             except NoSuchElementException:
#                 pass
            
#             #Price
#             try: 
#                 price = driver.find_element(By.CSS_SELECTOR, ".JPNOn").text
#             except NoSuchElementException:
#                 try:
#                     price = driver.find_element(By.CSS_SELECTOR, ".WXMFC").text
#                 except:
#                     pass
#                 pass
#             except StaleElementReferenceException: 
#                 pass
            
#             #Address
#             try: 
#                 address = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[6]/div/div/div/div/div/div[4]/div[1]/div[2]/span[2]/span").text
#             except NoSuchElementException:
#                 try: 
#                     address = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[2]/div/div[2]/div/div/div/span[2]/span").text
#                 except: 
#                     address = driver.find_element(By.CSS_SELECTOR, ".fHvkI").text
#                     pass
#                 pass
#             except StaleElementReferenceException:
#                 try: 
#                     address = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[2]/div/div[2]/div/div/div/span[2]/span").text
#                 except: 
#                     address = driver.find_element(By.CSS_SELECTOR, ".fHvkI").text
#                     pass
#                 pass
#             except ElementClickInterceptedException:
#                 try: 
#                     address = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[2]/div/div[2]/div/div/div/span[2]/span").text
#                 except: 
#                     address = driver.find_element(By.CSS_SELECTOR, ".fHvkI").text
#                     pass
#                 pass
            
#             #Description
#             try: 
#                 description = driver.find_element(By.CSS_SELECTOR, ".fIrGe").text
#             except NoSuchElementException: 
#                 try: 
#                     description = driver.find_element(By.CSS_SELECTOR, ".QewHA").text
#                 except:
#                     try: 
#                         description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[9]/div/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[3]/div[1]/div[1]/span").text                                          
#                     except:
#                         pass
#                     pass    
#                 pass
#             except StaleElementReferenceException: 
#                 try: 
#                     description = driver.find_element(By.CSS_SELECTOR, ".QewHA").text
#                 except:
#                     try: 
#                         description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[9]/div/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/div[3]/div[1]/div[1]/span").text                                          
#                     except:
#                         pass
#                     pass    
#                 pass
#             #Rank of province
#             try: 
#                 rank_of_province = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[1]/div[2]/div/a/span").text
#             except NoSuchElementException:
#                 pass
                
#             print("Address ---> ", address)    
#             data_list.append({
#                 "Title": title,
#                 "Price": price,
#                 "Rating": rating,
#                 "Address": address,
#                 "Img_URL": img_url,
#                 "Description": description,
#                 "Rank_of_province": rank_of_province,
#             })    
    
# Create DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Print the DataFrame
print(df)
df.to_csv('./data/crawlTripAdvisor4.csv', encoding='utf-8', index=False)