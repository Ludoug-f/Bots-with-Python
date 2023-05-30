from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

# Função para gerar uma lista de palavras aleatórias
def random_word_list(quantity):
    word_list = []
    
    for _ in range(quantity):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))
        word_list.append(word)
    
    return word_list

# Gerar uma lista de palavras aleatórias
str_list = random_word_list(30)

# Inicialização do driver do navegador
driver = webdriver.Edge()  # Substitua pelo driver do navegador de sua preferência

# Acessar o site do Bing
driver.get('https://bing.com')

# Aguardar a presença do elemento de entrada (campo de login)
entrar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_s')))
if entrar.is_displayed():
    entrar.click()

# Iterar sobre a lista de palavras aleatórias e pesquisar cada uma no Bing
for word in str_list:
    # Localizar o campo de pesquisa e limpar seu conteúdo
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
    search.clear()

    # Preencher o campo de pesquisa com a palavra atual
    search.send_keys(word)

    # Enviar a pesquisa
    search.submit()

    # Aguardar até que o título da página contenha a palavra pesquisada
    WebDriverWait(driver, 10).until(EC.title_contains(word))

# Fechar o navegador
driver.quit()
