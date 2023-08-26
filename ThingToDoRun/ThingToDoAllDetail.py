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

csv_file_path = 'D:/KLTN/TripAdvisor_Crawl/data/ThingToDo/Links/ThingTodoAllLinks.csv'
df = pd.read_csv(csv_file_path)
links_column = df['Link']
links_list = links_column.to_numpy()
print(links_list)

url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
# driver = webdriver.Chrome(service=service)

# PROXY = 'http://ip:port'
# chromeOptions = webdriver.ChromeOptions() 
# chromeOptions.add_argument('--proxy-server=%s' % PROXY) 
# chromeOptions.add_argument("ignore-certificate-errors")
# # Headless mode for chrome browser
# chromeOptions.add_argument('--headless=chrome')

driver = webdriver.Chrome(service=service) 
# driver.get("http://icanhazip.com")
# print(wbe.title)
# print(wbe.current_url)
# print(wbe.page_source)

# Create lists to store data
data_list = []
i = 0
for link in links_list:
    print('URL_PAGE_IN_FUNCTION: -----> ', link)
    title = -1
    price = -1
    rating = -1
    address = -1
    img_url = -1
    description = -1
    rank_of_province = -1
    link_thingtodo = -1
    
    sleep(random.randint(0,1))
    driver.get(link)
    
    link_thingtodo = link
    #Title
    try:
        title = driver.find_element(By.CSS_SELECTOR, ".iSVKr").text
    except NoSuchElementException:
        print("Exception No Such Element Title")
        pass
    except Exception as e:
        print("Exception Title: ", e)
        pass
    #Rating
    try:
        rating = driver.find_element("xpath", "/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[7]/div/div/div/section/section/div[1]/div/div[3]/div[1]/div/div[1]/div[1]").text
    except NoSuchElementException:
        try: 
            rating = driver.find_element("xpath", "/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[5]/div/div/div/section/section/div[1]/div/div[3]/div[1]/div/div[1]/div[1]").text
        except NoSuchElementException:
            print("Exception No Such Element Rating")
            pass
        except Exception as e:
            print("Exception Rating: ", e)
            pass
    except Exception as e:
        print("Exception Rating: ", e)
        pass
    #Image url
    try:
        img_url = driver.find_element("xpath", "/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/ul/li[1]/div/picture/img").get_attribute("src")
    except NoSuchElementException:
        try: 
            img_url = driver.find_element("xpath", "/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[2]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/ul/li[1]/button/div/picture/img").get_attribute("src")
        except NoSuchElementException:
            print("Exception No Such Element Image URL")
            pass
        except Exception as e:
            print("Exception Image URL: ", e)
            pass
    except Exception as e:
        print("Exception Image URL: ", e)
        pass
    #Price
    try: 
        price = -1
    except Exception as e: 
        print("Exception Price: ", e)
        pass
    #Address
    try: 
        address = driver.find_element("xpath", "/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[4]/div/div/div[2]/div[1]/div/div/div/div[1]/button/span").text
    except NoSuchElementException:
        print("Exception No Such Element Address")
        pass
    except Exception as e:
        print("Exception Address: ", e)
        pass
    #Description
    try: 
        description = driver.find_element("xpath", "/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[7]/div/div/div/section/section/div[1]/div/div[5]/div/div[1]/div/div/div[5]/div[1]/div").text
    except NoSuchElementException:
        try: 
            description = driver.find_element("xpath", "/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[7]/div/div/div/section/section/div[1]/div/div[5]/div/div[2]/div/div/div[5]/div[1]/div").text
        except NoSuchElementException:
            try: 
                description = driver.find_element("xpath", "/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[5]/div/div/div/section/section/div[1]/div/div[5]/div/div[2]/div/div/div[5]/div[1]/div/span").text
            except NoSuchElementException:
                print("Exception No Such Element Description")
                pass
            except Exception as e:
                print("Exception Description: ", e)
                pass
        except Exception as e:
            print("Exception Description: ", e)
            pass
    except Exception as e: 
        print("Exception Description: ", e)
        pass
    #Rank of province
    try: 
        rank_of_province = driver.find_element("xpath", "/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[1]/div/div/div/div/div[1]/div[2]/a/div").text
    except NoSuchElementException:
        print("Exception No Such Element Rank of province: ")
        pass
    except Exception as e:
        print("Exception Rank of province: ", e)
        rank_of_province = -1
        pass
    
    data_list.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Address": address,
        "Img_URL": img_url,
        "Description": description,
        "Rank_of_province": rank_of_province,
        "Link_ThingToDo": link_thingtodo,
    }) 
    df2 = pd.DataFrame(data_list)
    df2.to_csv('../data/ThingToDo/Details/ThingToDoAllDetails.csv', encoding='utf-8', index=False)
    i += 1
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii: --->>>>>>", i)
    if(i >= 100): break

df2 = pd.DataFrame(data_list)
df2.to_csv('../data/ThingToDo/Details/ThingToDoAllDetails.csv', encoding='utf-8', index=False)
