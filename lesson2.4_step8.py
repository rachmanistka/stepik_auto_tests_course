# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def func(x):
    return str(math.log(abs(12*math.sin(x))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    x = int(browser.find_element(By.ID, "input_value").text)
    y = func(x)
    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()