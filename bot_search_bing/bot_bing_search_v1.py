from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# # Função para gerar uma lista de palavras aleatórias
# def random_word_list(quantidade):
#     word_list = []
    
#     for _ in range(quantidade):
#         word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))
#         word_list.append(word)
    
#     return word_list

# # Gerar uma lista de palavras aleatórias
# gen_word_list = random_word_list(50)

#lista de palavras para testes
word_list = [
    'pronúncia', 'fotografar', 'feminicídio', 'limpador', 'facilitação',
    'psiquiatria', 'bisturi', 'agosto', 'polvo', 'inscrição',
    'corpúsculo', 'encarcerar', 'difundida', 'prendado', 'abrigo',
    'trigo', 'guitarrista', 'sopé', 'impaciente', 'concretizar',
    'agasalhado', 'pamonha', 'pacifista', 'penetração', 'multicolor',
    'república', 'futilidade', 'cantora', 'cancelado', 'quarentena'
    ]

# Criar uma instância do webdriver Edge
driver = webdriver.Edge()

# Abrir a página inicial do Bing
driver.get('https://bing.com')
time.sleep(1)

# Clicar no botão de login se estiver visível
entrar = driver.find_element(By.ID, 'id_s')
if entrar.is_displayed():
    entrar.click()
time.sleep(1)

# Realizar searchs para cada palavra na lista gerada
for word in word_list:
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
    search.clear()
    search.send_keys(word)
    search.submit()
    time.sleep(2)

# Aguardar 2 segundos antes de fechar o navegador
time.sleep(2)
driver.quit()
