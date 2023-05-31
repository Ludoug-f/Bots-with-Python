from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

def random_word_list(quantity):
    word_list = []
    
    for _ in range(quantity):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))
        word_list.append(word)
    
    return word_list

str_list = random_word_list(30)

driver = webdriver.Edge()

driver.get('https://bing.com')
time.sleep(1)

entrar = driver.find_element(By.ID, 'id_s')
if entrar.is_displayed():
    entrar.click()
time.sleep(1)

for word in str_list:
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
    search.clear()
    search.send_keys(word)
    search.submit()
    time.sleep(1)

time.sleep(3)
driver.quit()