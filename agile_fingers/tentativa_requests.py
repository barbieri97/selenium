# Aqui e tentei coletar o texto atrávés da biblioteca requests e BeautifulSoup
# Mas como a pagina é carregada dinamicamente através de java script tive dificuldades em dar continuidade

import requests
from bs4 import BeautifulSoup

r = requests.get("https://agilefingers.com/texts/a-l-o-e-beyond-the-black-waters-en")

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.find("span", id="modelText2ndLineText"))