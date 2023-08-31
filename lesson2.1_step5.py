# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_el.text
    y = calc(x)
    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(y)
    checkbox = browser.find_element(By.CLASS_NAME, "form-check-label")
    checkbox.click()
    selectbox = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    selectbox.click()
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