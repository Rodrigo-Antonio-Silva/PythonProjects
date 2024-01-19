import pandas as pd
import sqlite3

conn = sqlite3.connect('/home/rodrigo/git_workplace/OpenClassRoom/django-web-app/merchex/db.sqlite3')
cursor = conn.cursor()

data = pd.read_csv('/home/rodrigo/git_workplace/PythonProjects/pythonProject/bandas2.csv')
lista = data['artist'].unique()

# print(lista)
for i, cantor in enumerate(lista):

    cursor.execute('INSERT OR IGNORE INTO listings_singers (id, name) VALUES (?, ?)', (i + 1, cantor))

conn.commit()

conn.close()

