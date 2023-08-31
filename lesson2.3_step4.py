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
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = int(browser.find_element(By.ID, "input_value").text)
    y = func(x)
    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

   

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()