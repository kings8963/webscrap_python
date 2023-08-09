import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
url = "https://pokemondb.net/pokedex/all"
response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

rows = soup.find('table', attrs={"id":"pokedex"}).find("tbody").find_all('tr')
print(rows[0].find_all('td')[1].get_text())

names =[]
types = []
total = []
hp = []
attacks = []
defense = []

for row in rows:
    names.append(row.find_all('td')[1].get_text())
    types.append(row.find_all('td')[2].get_text())
    total.append(row.find_all('td')[3].get_text())
    hp.append(row.find_all('td')[4].get_text())
    attacks.append(row.find_all('td')[5].get_text())
    defense.append(row.find_all('td')[6].get_text())

df = pd.DataFrame({"Nombre":names,
                   "Tipo":types,
                   "Total":total,
                   "hp":hp,
                   "Attack":attacks,
                   "Defensa":defense
                   })

df.to_csv('pokemon.csv')

"""
#print(df)
url = "http://192.168.0.199:8000/"
response = requests.get(url)


contenido = response.text
#print(contenido)

"""
rows = soup.find('table', attrs={"id":"pokedex"}).find("tbody").find_all('tr')
print(rows[0].find_all('td')[1].get_text())
"""



soup = BeautifulSoup(response.content,'html.parser')
div = soup.find('div', id= 'paperInfomationModule').find('tbody').find_all('tr')
#tabla = div[0].find_all('td')
#print(div[0].find_all('th')[1].get_text())
"""
for file in div:
    celdas = file.find_all('th')
    for celda in celdas:
        print(celda.get_text())

"""



print(div)