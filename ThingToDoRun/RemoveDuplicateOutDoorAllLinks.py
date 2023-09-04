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

csv_file_path = 'D:/KLTN/TripAdvisor_Crawl/data/ThingToDo/Links/OutDoorAllLinks.csv'
df = pd.read_csv(csv_file_path)
df.drop_duplicates(subset=None, inplace=True)
df.to_csv('D:/KLTN/TripAdvisor_Crawl/data/ThingToDo/Links/RemovedDuplicateOutDoorAllLinks.csv', index=False)