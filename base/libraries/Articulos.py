from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def open_web(search):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.mercadolibre.com.uy/")
    sleep(5)
    search_box = driver.find_element(By.NAME, "as_word")
    search_box.send_keys(search)
    search_box.submit()
    articulos = get_articulos(driver)
    sleep(5)
    return articulos

def get_articulos(driver):
    elements = driver.find_elements(By.XPATH, "//li[contains(@class,'search-layout')]//a")
    articulos = []
    
    for element in elements:
        link = element.get_attribute('href')
        print(link)
        articulos.append(link)
   
    return articulos