import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

data = pd.read_csv('bandas2.csv')

cantores = data['artist']

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get(f'http://127.0.0.1:8000/admin//')

# user
driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('rodrigo')
# password
driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('Ro200202292641')
#botão
driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()

sleep(3)

y = 19
for i in range(159, 209):
    driver.get(f'http://127.0.0.1:8000/admin/listings/band/{i}/change/')

    find_singer = \
    driver.find_element(By.ID, "id_singer")
    select_singer = Select(find_singer)
    select_singer.select_by_visible_text(cantores[y])

    driver.find_element(By.XPATH, '/html/body/div/div/main/div[1]/div/form/div/div/input[1]').click()
    y += 1


