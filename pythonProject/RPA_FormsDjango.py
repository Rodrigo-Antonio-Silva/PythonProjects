import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

data = pd.read_csv('bandas2.csv')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('http://127.0.0.1:8000/admin/listings/band/add/  ')


# user
driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('rodrigo')

# password
driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('Ro200202292641')

#botão
driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()

#acessar banco
#driver.find_element(By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr/td[1]/a').click()

sleep(3)

for i, titulo in enumerate(data['title']):
    title = data.loc[i, 'title']
    artist = data.loc[i, 'artist']
    genre = data.loc[i, 'genre']
    off_site = data.loc[i, 'site']
    year = data.loc[i, 'year']
    description = data.loc[i, 'description']
    status = data.loc[i, 'status']
    sold = data.loc[i, 'sold']
    type = data.loc[i, 'type']
    sleep(1)

    # artista
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[1]/div/div/input').send_keys(artist)
    sleep(1)

    # musica
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[2]/div/div/input').send_keys(title)
    sleep(1)

    # genero
    find_genre = \
    driver.find_element(By.ID, "id_genre")
    select_genre = Select(find_genre)
    select_genre.select_by_visible_text(genre)

    # descrição
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[4]/div/div/input').send_keys(description)
    sleep(1)

    # Ano
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[5]/div/div/input').clear()
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[5]/div/div/input').send_keys(int(year))
    sleep(1)

    # ativo
    if status == 'Active':
        driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[6]/div/div/input').click()
    sleep(1)

    # site
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[7]/div/div/input').send_keys(off_site)
    sleep(1)

    #sold
    if sold == 'Yes':
        driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[8]/div/div/input').click()
    sleep(1)

    # Ano2
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[9]/div/div/input').clear()
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/fieldset/div[9]/div/div/input').send_keys(int(year))
    sleep(1)

    # tipo
    find_type = \
    driver.find_element(By.ID, "id_type")
    select_type = Select(find_type)
    select_type.select_by_visible_text(type)
    sleep(1)

    # botão (save and add)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/div/input[2]').click()

# botão (SAVE)
driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/div/input[1]').click()
