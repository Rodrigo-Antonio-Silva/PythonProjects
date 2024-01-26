import pandas as pd
import sqlite3

conn = sqlite3.connect('/home/rodrigo/git_workplace/OpenClassRoom/django-web-app/merchex/db.sqlite3')

cursor = conn.cursor()

cursor.execute('SELECT name FROM listings_singers')

data = pd.read_csv('/home/rodrigo/git_workplace/PythonProjects/pythonProject/bandas2.csv')

df = data.drop_duplicates(subset='artist')

df = df[['artist', 'status', 'description', 'genre', 'site', 'year']]

singers = df[~df['artist'].isin(['James Arthur', 'Labrinth'])]
# print(singers['status'])
for i, cantor in enumerate(singers['artist']):
    #print(i)
    cursor.execute(
        f"UPDATE listings_singers SET year_formed = {int(singers.iloc[i, 5])} WHERE name = '{cantor}'")

conn.commit()

conn.close()
