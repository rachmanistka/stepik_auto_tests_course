# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error")
        
if __name__ == "__main__":
    unittest.main()