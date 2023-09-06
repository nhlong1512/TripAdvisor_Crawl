from ctypes.wintypes import SERVICE_STATUS_HANDLE
import time
import numpy as np
from selenium import webdriver
from time import sleep
import random
import os
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

csv_file_path = 'D:/NPVSCode/CrawlData/TripAdvisor_Crawl/data/Food/Links/AllLinksFoodClean.csv'
df = pd.read_csv(csv_file_path)
links_column = df['Link']
links_list = links_column.to_numpy()
print(links_list)


profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
url_file_driver = os.path.join('etc', 'geckodriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver, firefox_profile=profile)
driver = webdriver.Firefox(service=service)


# Create lists to store data
data_list = []
i = 0
for link in links_list:
    if(i <= 1132): 
        i += 1
        continue
    print('URL_PAGE_IN_FUNCTION: -----> ', link)
    title = -1
    price = -1
    rating = -1
    address = -1
    img_url = -1
    description = -1
    rank_of_province = -1
    link_food = -1
    
    driver.get(link)
    link_food = link
    start_time = time.time()  # Lưu thời điểm bắt đầu tải trang
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > 5:  # Nếu thời gian tải trang vượt quá 5 giây
            print("Page loading took too long, moving to next URL.")
            break  # Thoát khỏi vòng lặp để chuyển sang URL tiếp theo
        # Kiểm tra xem trang đã tải xong chưa, ví dụ kiểm tra title hay một phần tử nào đó
        try:
            title_element = driver.find_element(By.CSS_SELECTOR, ".HjBfq")
            if title_element.is_displayed():
                break  # Thoát khỏi vòng lặp vì trang đã tải xong
        except Exception:
            pass
        
        # Chờ một khoảng thời gian rồi kiểm tra lại
        time.sleep(1)
    
    #Title
    try:
        title = driver.find_element(By.CSS_SELECTOR, ".HjBfq").text
    except NoSuchElementException:
        print("Exception No Such Element Title")
        pass
    except Exception as e:
        print("Exception Title: ", e)
        pass
    #Rating
    try:
        rating = driver.find_element(By.CSS_SELECTOR, ".ZDEqb").text
    except NoSuchElementException:
        try:
            rating = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/span[1]").text
        except NoSuchElementException:
            print("ExceptionNoSuchElement Rating")
            pass
    except Exception as e:
        print("Exception Rating: ", e)
        pass
    #Image url
    try:
        img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/img").get_attribute("src")
    except NoSuchElementException:
        try: 
            img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div[3]/div/div/img").get_attribute("src")
        except NoSuchElementException:
            try: 
                img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/div/div[1]/div/div/img").get_attribute("src")
            except NoSuchElementException: 
                try: 
                    img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div[3]/div/div[3]/div/div/img").get_attribute("src")
                except NoSuchElementException: 
                    try: 
                        img_url = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div[3]/div/div[4]/div/div/img").get_attribute("src")
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
        address = driver.find_element(By.CSS_SELECTOR, ".yEWoV").text
    except NoSuchElementException:
        try:
            address = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[3]/div/div/div[1]/span[2]/a/span[1]").text
        except NoSuchElementException:
            try:
                address = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[4]/div/div/div[3]/span[1]/span/a").text
            except NoSuchElementException:
                try: 
                    address = driver.find_element(By.CSS_SELECTOR, ".AYHFM").text
                except NoSuchElementException:
                    print("Exception No Such Element Address")
                    pass
    except Exception as e:
        print("Exception Address: ", e)
        pass
    #Description
    try: 
        description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[6]/div/div[1]/div[3]/div/div[5]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/p").text
    except NoSuchElementException:
        try: 
            description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[6]/div/div[1]/div[3]/div/div[5]/div/div[3]/div[5]/div/div/div/div[2]/div[2]/div/p").text
        except NoSuchElementException:
            try: 
                description = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[3]/div[2]").text
            except NoSuchElementException:
                try:
                    description = driver.find_element(By.CSS_SELECTOR, ".SrqKb").text
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
        rank_of_province = driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[4]/div/div/div[2]/span[2]/a/span").text
    except NoSuchElementException:
        try: 
            rank_of_province = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[1]/div[2]").text
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
        "Link_Food": link_food,
    }) 
    
    
    df2 = pd.DataFrame(data_list)
    df2.to_csv('../data/Food/Details/FoodAllDetails2.csv', encoding='utf-8', index=False)
    i += 1
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii: --->>>>>>", i)
    if(i >= 16418): break

driver.close()
df2 = pd.DataFrame(data_list)
df2.to_csv('../data/Food/Details/FoodAllDetails2.csv', encoding='utf-8', index=False)
