# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    nameInput = browser.find_element(By.CSS_SELECTOR, ".form-control first")
    nameInput.send_keys("AB")

    lastnameInput = browser.find_element(By.CSS_SELECTOR, ".form-control second")
    lastnameInput.send_keys("AB")

    emailInput = browser.find_element(By.CSS_SELECTOR, ".form-control third")
    emailInput.send_keys("AB")

    # ���������� ����������� �����
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

    # ������� �������, ���������� �����
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # ���������� � ���������� welcome_text ����� �� �������� welcome_text_elt
    welcome_text = welcome_text_elt.text

    # � ������� assert ���������, ��� ��������� ����� ��������� � ������� �� �������� �����
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()