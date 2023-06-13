# Bing_Search

## Description

Bot para fazer pesquisas no Bing usando palavras geradas aleatoriamente, feito para adquirir pontos no Microsoft Rewards.

Atenção: o bot foi testado apenas no edge, mas deve funcionar em qualquer navegador que tenha suporte ao selenium

O bot segue os seguintes passos:

1. Abre o navegador
2. Acessa o site do Bing
3. Faz login na conta da Microsoft se nao estiver logado
4. Atualiza a pagina para garantir que esta aparecendo os pontos
5. Salva o valor dos pontos atuais e analisa quantos pontos faltam
6. Realiza a primeira pesquisa usando uma palavra pre definida
7. Na pagina de busca salva o valor dos pontos atuais e analisa quantos pontos faltam e inicia um loop
8. No loop enquanto o valor dos pontos atuais for diferente do valor pretendido ele realiza uma nova pesquisa usando uma palavra gerada aleatoriamente

 
 ---
## Requirements

- Python 3.10.0
- Selenium 4.9.1

---
## How to use

1. Clone to repositório

```bash
git clone git@github.com:Ludoug-f/Bots-with-Python.git
```

2. Instale os requirements

```bash
pip install selenium # or pip3 install selenium
```

3. baixe o webdriver do navegador que você deseja usar e coloque na pasta do projeto

Opcional: Por padrão o bot esta configurado para pesquisar ate atingir *90* pontos, para alterar o valor basta alterar a variavel *VALOR* no arquivo *bot_bing_search.py* na linha 9

```python

4. Execute o script

```bash
python bot_bing_search.py # or python3 bot_bing_search.py
```
