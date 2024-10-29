from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium import webdriver 
from time import sleep


def load_data_ine(p, url):

    periodo = str(p[1])
    
    chrome_options = webdriver.ChromeOptions()

    directorio_guardado = "C:\\Users\\Administrador\\Desktop\\RCM\\laboratorio-modulo5-leccion01-elt-extraccion\\data\\ine"

    prefs = {
        "download.default_directory": directorio_guardado, 
        "download.prompt_for_download": False, 
        "directory_upgrade": True, 
        "safebrowsing.enabled": True
    }

    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(chrome_options)
    driver.get(url)
    sleep(5)
    driver.find_element('css selector','#aceptarCookie').click()
    driver.implicitly_wait(10)
    driver.find_element("css selector", f'#periodo > option:nth-child({periodo})').click()
    driver.implicitly_wait(10)
    driver.find_element("css selector", '#botonConsulSele').click()
    driver.implicitly_wait(10)
    driver.find_element('xpath','/html/body/div[1]/main/ul/li/div/div/form[2]/button').click()
    driver.implicitly_wait(10)
    sleep(5)
    driver.find_element('xpath','//*[@id="export"]/ul/li[4]/label').click()
    sleep(5)
    driver.close()

def main(parametros, url):
    for i in parametros:
        load_data_ine(i, url)

