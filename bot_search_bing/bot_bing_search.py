from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

VALOR = 90

## Função para gerar uma lista de palavras aleatórias
# def random_word_list(quantidade):
#     word_list = []
    
#     for _ in range(quantidade):
#         word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))
#         word_list.append(word)
    
#     return word_list

# Função para gerar uma palavra aleatória
def random_word():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))

# Criar uma instância do webdriver Edge
driver = webdriver.Edge()

# Abrir a página inicial do Bing
driver.get('https://bing.com')

# Clicar no botão de login se estiver visível
entrar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_s')))
if entrar.is_displayed():
    entrar.click()
    print("clicou em entrar")

logado = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_n')))
if logado.is_displayed():
    print("logado")

time.sleep(1)
## atualizar a pagina
driver.refresh()
time.sleep(3)

# Obter a quantidade inicial de pontos
init_points = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_rc')))
init_points_num = int(init_points.text)
print("inicial", init_points_num)

# Definir a quantidade de pontos desejada
sum_points = init_points_num + VALOR

# Realizar uma pesquisa inicial
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
search.send_keys('udyr')
search.submit()

# Obter a quantidade atual de pontos
current_points = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_rc')))
current_points_num = int(current_points.text)

# Realizar pesquisas adicionais até atingir a quantidade desejada de pontos
while current_points_num != sum_points:
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
    search.clear()
    search.send_keys(random_word())
    search.submit()
    current_points = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_rc')))
    current_points_num = int(current_points.text)
    time.sleep(1)
    print(f"{current_points_num} / {sum_points}")

## Realizar a última pesquisa de garantia
# search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
# search.clear()
# search.send_keys(random_word())
# search.submit()

time.sleep(3)

driver.quit()