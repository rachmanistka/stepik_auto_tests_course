# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

def func(x):
    return str(math.log(abs(12*math.sin(x))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.NAME, "firstname")
    first.send_keys("dar")

    second = browser.find_element(By.NAME, "lastname")
    second.send_keys("iv")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("@")
    element = browser.find_element(By.XPATH, "//input[@type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)   
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()