from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import random

def Get_Pokenames():
    try:
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1000')
        if response.status_code == 200:
            pokemons = response.json()['results']
            return [pokemon['name'] for pokemon in pokemons]
        else:
            print('Erro ao obter nomes dos pokemons')
    except requests.exceptions.RequestException as e:
        return print(f'Erro ao obter nomes dos pokemons: {e}')
    
Pokenames = Get_Pokenames()
random.shuffle(Pokenames)
Pokenames = Pokenames[:50]

def search():
    # Criar uma instância do webdriver Edge
    driver = webdriver.Edge()
    
    # Navegar até a página do Bing
    driver.get('https://bing.com')

    # aguardar usuário logar
    input('Pressione enter para continuar...')

    counter = 0

    # Realiza uma pesquisa pra cada nome de pokemon
    for name in Pokenames:
        driver.get('https://bing.com')
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
        search_box.clear()
        search_box.send_keys(name)
        search_box.submit()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b_results')))
        time.sleep(300) # Aguardar 5 minutos

    # Aguardar 2 segundos antes de fechar
    time.sleep(2)

    # Fechar o navegador
    driver.quit()

if __name__ == '__main__':
    search()
