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


csv_file_path2 = 'D:/NPVSCode/CrawlData/TripAdvisor_Crawl/data/Food/Links/NumberFoodsProvince.csv'
df2 = pd.read_csv(csv_file_path2)
number_column = df2['Number_Food']
number_list = number_column.to_numpy()
print('NUMBER__LISTSSSSSSSSSSSSSSSSSS',number_list)
print(number_column)


profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
url_file_driver = os.path.join('etc', 'geckodriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver, firefox_profile=profile)
driver = webdriver.Firefox(service=service)
# Create lists to store data
data_list = []
rich_food_links = []

def crawl_one_page(url_page): 
    # Open URL
    print('URL_PAGE_IN_FUNCTION: -----> ', url_page)
    driver.get(url_page)
    sleep(random.randint(3,5))
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, ".biGQs [href]")
        links = [elem.get_attribute('href') for elem in elems]
        print(links)
        for link in links: 
            if link == 'https://tripadvisor.mediaroom.com/VN-terms-of-use' or link == 'https://tripadvisor.mediaroom.com/vn-privacy-policy' or link == 'https://www.tripadvisor.com.vn/SiteIndex-g293921-Vietnam.html' or link == 'https://www.tripadvisor.com.vn/pages/service_en.html' or link == 'https://tripadvisor.mediaroom.com/VN-contact-us': 
                continue
            rich_food_links.append({"Link": link})
        df = pd.DataFrame(rich_food_links)
        df.to_csv('../data/Food/Links/AllLinksFood2.csv', encoding='utf-8', index=False)
    except Exception as e:
        print('Exception: 1234567890')
        pass

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
        return new_link
    else:
        print("Không tìm thấy chuỗi số-chữ trong URL.")
        return "Không tìm thấy chuỗi số-chữ trong URL."

def get_all_links(qty, link):
    crawl_one_page(link)
    for page_oa in range(30,qty,30): 
        urlPage = generate_link(link, page_oa)
        print('URL PAGE GET ALL LINKS', urlPage)
        crawl_one_page(urlPage) 

    

i=2
for link in links_list:
    if i < 240: 
        i += 1
        continue
    print("\nLINK ---> ", link, "NUMBER_LINK_FOOD ---> ", number_list[i-2])
    get_all_links(number_list[i-2], link)
    i += 1
    if i >263: 
        break
 

     
        


    # df2 = pd.DataFrame(data_list)
    # df2.to_csv('./data/CrawlTripAdvisor_Hotels_All_1.csv', encoding='utf-8', index=False)

# df2 = pd.DataFrame(data_list)
# df2.to_csv('./data/CrawlTripAdvisor_Hotels_All_1.csv', encoding='utf-8', index=False)