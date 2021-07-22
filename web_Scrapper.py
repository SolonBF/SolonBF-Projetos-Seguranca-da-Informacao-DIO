from bs4 import BeautifulSoup

import requests

# O objeto site recebendo o conteudo da requisicao http do site
site = requests.get('https://www.climatempo.com.br/').content

# Baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

# Transforma o html em string e o print mostra na tela.
# print(soup.prettify())

temperatura = soup.find('span', class_ = '_block _margin-b-5 -gray')

print(soup.title.string)