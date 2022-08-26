from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from numpy import random
import time
import pandas as pd

contatos = pd.read_excel("grupos.xlsx")
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
mensagems = contatos.loc[0, "Mensagem"]
navegador.get("https://web.whatsapp.com/")


while len(navegador.find_elements(By.ID, value='side')) < 1:
    time.sleep(1)


for i,message in enumerate(contatos["Grupo"]):
    group = contatos.loc[i, "Grupo"]

    while not(navegador.find_elements(By.XPATH,value='//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')):
        time.sleep(1)

    navegador.find_elements(By.XPATH,value='//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    navegador.find_element(By.XPATH,value='//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').click()
    navegador.find_element(By.XPATH,value='//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(group)
    navegador.find_element(By.XPATH,value='//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(Keys.ENTER)

    while not(navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')):
        time.sleep(1)


    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').click()
    if navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'):
        navegador.find_element(By.XPATH,value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(mensagems)
        time.sleep(1)
        navegador.find_element(By.XPATH,value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(Keys.ENTER)
        numeroRand = random.randint(10)
        time.sleep(numeroRand)
    else:
        numeroRand = random.randint(10)
        time.sleep(numeroRand)