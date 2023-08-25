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

csv_file_path = 'D:/KLTN/TripAdvisor_Crawl/data/Food/Links/LinkPageProvinces.csv'
df = pd.read_csv(csv_file_path)
links_column = df['link']
links_list = links_column.to_numpy()
print(links_list)
print(links_column)

url_file_driver = os.path.join('etc', 'chromedriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
driver = webdriver.Chrome(service=service)
# Create lists to store data
data_list = []


# Phân tích chuỗi URL
def generate_link(link, number_oa):
    pattern = r'(\d+)-([A-Za-z])'
    matches = re.search(pattern, link)
    if matches:
        original_text = matches.group(0)  # Chuỗi gốc tìm thấy
        number_part = matches.group(1)  # Phần số trong chuỗi
        letter_part = matches.group(2)  # Phần chữ trong chuỗi
        # Thêm 'oa30' vào giữa số và chữ
        new_text = f'{number_part}-oa'+str(number_oa)+f'-{letter_part}'
        # Thay thế chuỗi gốc bằng chuỗi mới
        new_link = link.replace(original_text, new_text)
        print("New__Link",new_link)
    else:
        print("Không tìm thấy chuỗi số-chữ trong URL.")


def crawl_one_page(url_page): 
    # Open URL
    print('URL_PAGE_IN_FUNCTION: -----> ', url_page)
    driver.get(url_page)
    sleep(random.randint(10,15))
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, ".biGQs [href]")
        links = [elem.get_attribute('href') for elem in elems]
        print(links)
        df = pd.DataFrame(links)
        df.to_csv('../data/Food/Links/AllLinksFood.csv', encoding='utf-8', index=False)
    except Exception as e:
        print('Exception: 1234567890')
        pass
    
def get_all_links(qty, link):
    for page_oa in range(30,qty,30): 
        urlPage = generate_link(link, page_oa)
        print('URL PAGE GET ALL LINKS', urlPage)
        # crawl_one_page(urlPage) 

for link in links_list:
    crawl_one_page(link)
    get_all_links(601, link)
    # try: 
    #     restaurant_qty = driver.find_element("xpath", "/html/body/div[1]/main/div/div[4]/div/div/div/div[2]/div[1]/div[1]/div/div/span/span").text
    #     # get_all_links(int(restaurant_qty), link)
    #     print(restaurant_qty)
    #     break
    # except Exception as e:
    #     print("Exception: ", e)
    #     pass
 

     
        


    # df2 = pd.DataFrame(data_list)
    # df2.to_csv('./data/CrawlTripAdvisor_Hotels_All_1.csv', encoding='utf-8', index=False)

# df2 = pd.DataFrame(data_list)
# df2.to_csv('./data/CrawlTripAdvisor_Hotels_All_1.csv', encoding='utf-8', index=False)