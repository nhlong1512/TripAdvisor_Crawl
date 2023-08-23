from ctypes.wintypes import SERVICE_STATUS_HANDLE
from selenium import webdriver
import datetime
import os
import time

if __name__ == "__main__":
    url_file_driver = os.path.join('etc', 'chromedriver.exe')
    service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver)
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.tripadvisor.com/Hotels-g293921-Vietnam-Hotels.html")
    
    target = driver.find_element("xpath","/html/body/div[1]/main/div[3]/div/div[2]/div/div[1]/div[2]/div[3]/div")
    for data in target:
        # images = data.find_elements_by_class_name("NhWcC _R mdkdE")
        titles = data.find_elements_by_class_name("nBrpc Wd o W")
    
    # for  i in images: 
    #     print(i.text)
    print('Target --->   ', target);
    
    for i in titles: 
        print('Text title      ------->     ', i)
    
    # time.sleep(4)
    driver.close()
