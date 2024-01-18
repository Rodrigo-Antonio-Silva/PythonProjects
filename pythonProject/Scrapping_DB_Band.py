import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

data = pd.read_csv('/home/rodrigo/Jupyter/bandas.csv')


lista = data['artist'].unique()
print(lista)
nova_lista = []
descricao = []
sites = []

for palavra in lista:
    if palavra.count(" ") > 0:
        nova_palavra = "_".join(palavra.split(" "))
        nova_lista.append(nova_palavra)
    else:
        nova_lista.append(palavra)

#print(nova_lista)
for i in nova_lista:
    html = urlopen(f'https://pt.wikipedia.org/wiki/{i}')
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.prettify())
    descr = bs.findAll("p")[1]
    print(descr.text)
    descricao.append(descr.text)

    try:
        span = bs.find('span', class_='official-website')
        a = span.find('a')
    except:
        a = bs.find('a', class_='external text')

    href = a['href']
    print(href)
    sites.append(href)

#print(len(descricao))
#print(len(sites))

data = data.assign(description=pd.Series([None] * len(data)))
data = data.assign(site=pd.Series([None] * len(data)))

#print(data.head())

for i, cantor in enumerate(data['artist']):
    print(cantor)
    if cantor == 'Bruno Mars':
        data.loc[i, 'description'] = descricao[0]
        data.loc[i, 'site'] = sites[0]
    elif cantor == 'Maroon 5':
        data.loc[i, 'description'] = descricao[1]
        data.loc[i, 'site'] = sites[1]
    elif cantor == 'Neon Trees':
        data.loc[i, 'description'] = descricao[2]
        data.loc[i, 'site'] = sites[2]
    elif cantor == 'Taylor Swift':
        data.loc[i, 'description'] = descricao[3]
        data.loc[i, 'site'] = sites[3]
    elif cantor == 'Owl City':
        data.loc[i, 'description'] = descricao[4]
        data.loc[i, 'site'] = sites[4]
    elif cantor == 'James Arthur':
        data.loc[i, 'description'] = descricao[5]
        data.loc[i, 'site'] = sites[5]
    elif cantor == 'Labrinth':
        data.loc[i, 'description'] = descricao[6]
        data.loc[i, 'site'] = sites[6]
    elif cantor == 'Sam Smith':
        data.loc[i, 'description'] = descricao[7]
        data.loc[i, 'site'] = sites[7]
    elif cantor == 'MAGIC!':
        data.loc[i, 'description'] = descricao[8]
        data.loc[i, 'site'] = sites[8]
    elif cantor == 'Passenger (cantor)':
        data.loc[i, 'description'] = descricao[9]
        data.loc[i, 'site'] = sites[9]
    elif cantor == 'John Newman':
        data.loc[i, 'description'] = descricao[10]
        data.loc[i, 'site'] = sites[10]
    elif cantor == 'Michael Jackson':
        data.loc[i, 'description'] = descricao[11]
        data.loc[i, 'site'] = sites[11]
    elif cantor == 'Ed Sheeran':
        data.loc[i, 'description'] = descricao[12]
        data.loc[i, 'site'] = sites[12]
    elif cantor == 'Wiz Khalifa':
        data.loc[i, 'description'] = descricao[13]
        data.loc[i, 'site'] = sites[13]
    elif cantor == 'G-Eazy':
        data.loc[i, 'description'] = descricao[14]
        data.loc[i, 'site'] = sites[14]
    elif cantor == 'Cardi B':
        data.loc[i, 'description'] = descricao[15]
        data.loc[i, 'site'] = sites[15]
    elif cantor == 'Dan + Shay':
        data.loc[i, 'description'] = descricao[16]
        data.loc[i, 'site'] = sites[16]
    elif cantor == 'N.E.R.D':
        data.loc[i, 'description'] = descricao[17]
        data.loc[i, 'site'] = sites[17]
    elif cantor == 'Lewis Capaldi':
        data.loc[i, 'description'] = descricao[18]
        data.loc[i, 'site'] = sites[18]
    else:
        data.loc[i, 'description'] = descricao[19]
        data.loc[i, 'site'] = sites[19]


print(data.head())
data.to_csv('bandas2.csv', index=False)
