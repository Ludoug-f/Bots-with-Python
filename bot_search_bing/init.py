from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

driver = webdriver.Edge()

driver.get('https://bing.com')

time.sleep(99999)