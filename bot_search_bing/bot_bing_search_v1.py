from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
time.sleep(2)

entrar = driver.find_element(By.ID, 'id_s')
if entrar.is_displayed():
    entrar.click()
time.sleep(2)

for word in str_list:
    search = driver.find_element(By.ID, 'sb_form_q')
    search.send_keys(word)
    search.submit()
    time.sleep(3)

time.sleep(3)
driver.quit()