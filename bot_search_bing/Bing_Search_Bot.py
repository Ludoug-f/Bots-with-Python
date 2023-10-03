from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# Função para gerar uma string aleatória
def random_str():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))

# Criar uma instância do webdriver Edge
driver = webdriver.Edge()

# Abrir a página inicial do Bing
driver.get('https://bing.com')

# Solicita ao usuário que insira um valor e armazena na variável
input_qnt = input("digite a quantidade de pesquisas que deseja realizar: ")
search_qnt = int(input_qnt)

# Realizar pesquisas até atingir a quantidade desejada
for i in range(search_qnt):
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
    search_box.clear()
    search_box.send_keys(random_str())
    search_box.submit()
    search_results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b_results')))
    time.sleep(0.5)

# Aguardar 1 segundos antes de fechar
time.sleep(1)

# Fechar o navegador
driver.quit()
