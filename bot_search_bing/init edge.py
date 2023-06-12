from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# Criar uma instância do webdriver Edge
driver = webdriver.Edge()

# Abrir a página inicial do Bing
driver.get('https://bing.com')

# Clicar no botão de login se estiver visível
entrar = driver.find_element(By.ID, 'id_s')
if entrar.is_displayed():
    entrar.click()
time.sleep(1)

## atualizar a pagina
driver.refresh()
time.sleep(2)

init_points = driver.find_element(By.ID, 'id_rc')
init_points_num = int(init_points.text)
print(init_points_num)

sum_points = init_points_num + 90

time.sleep(2)

search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
search.send_keys('teste')
search.submit()
time.sleep(1)

lated_points = driver.find_element(By.ID, 'id_rc')
lated_points_num = int(lated_points.text)

while lated_points_num != sum_points:
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
    search.clear()
    search.send_keys('teste')
    search.submit()
    time.sleep(1)
    lated_points = driver.find_element(By.ID, 'id_rc')
    lated_points_num = int(lated_points.text)
    print(lated_points_num)


time.sleep(500)