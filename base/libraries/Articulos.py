from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def open_web():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://listado.mercadolibre.com.uy/notebook#D[A:notebook]")
    sleep(5)
    articulos = get_articulos(driver)
    print(articulos)
    sleep(5)
    return articulos

def get_articulos(driver):
    elements = driver.find_elements(By.XPATH, "//ol/li/div/div/div/a")
    articulos = []
    
    for element in elements:
        descripcion_web = element.find_element(By.XPATH, ".//a[@href]")

        articulos.append(descripcion_web)

    return articulos 