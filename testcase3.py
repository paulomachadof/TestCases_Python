# Test Case ID = ID_003
# Test Case Description: Fazer Cadastro com senhas diferentes.
#autor: paulomachado

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class TestFunc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/home/paulo/Downloads/geckodriver')
        self.driver.implicitly_wait(30)
        self.base_url = "http://med-profile.apps.intmed.com.br/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_func(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Cadastro").click()
        search_field = driver.find_element_by_id("user_name")
        search_field.send_keys("Paulo Machado")
        search_field1 = driver.find_element_by_id("user_cpf")
        search_field1.send_keys("00100200304")
        search_field2 = driver.find_element_by_id("user_phone")
        search_field2.send_keys("8533333333")
        search_field3 = driver.find_element_by_id("user_email")
        search_field3.send_keys("email123@email.com")
        search_field4 = driver.find_element_by_id("user_password")
        search_field4.send_keys("senha1")
        search_field5 = driver.find_element_by_id("user_password_confirmation")
        search_field5.send_keys("senhadiferente")
        driver.find_element_by_xpath("/html/body/div/div[2]/form/div[7]/div[2]/input").click()

if __name__ == "__main__":
    unittest.main()
