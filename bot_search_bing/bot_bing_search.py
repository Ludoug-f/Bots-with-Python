from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# def random_word_list(quantidade):
#     word_list = []
    
#     for _ in range(quantidade):
#         word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))
#         word_list.append(word)
    
#     return word_list

def random_word():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))

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
time.sleep(3)

init_points = driver.find_element(By.ID, 'id_rc')
init_points_num = int(init_points.text)
print("inicial", init_points_num)

sum_points = init_points_num + 15

time.sleep(2)

search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
search.send_keys('udyr')
search.submit()
time.sleep(1)

current_points = driver.find_element(By.ID, 'id_rc')
current_points_num = int(current_points.text)

while current_points_num != sum_points:
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
    search.clear()
    search.send_keys(random_word())
    search.submit()
    time.sleep(2)
    current_points = driver.find_element(By.ID, 'id_rc')
    current_points_num = int(current_points.text)
    print("soma", sum_points)
    print("atual", current_points_num)


time.sleep(2)