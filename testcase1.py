#Test Case ID = ID_001
# Test Case Description: Cliente tenta logar com e-mail não cadastrado.
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
        search_field = driver.find_element_by_id("user_email")
        search_field.send_keys("email@email.com")
        search_field.submit()
        driver.find_element_by_link_text("Entrar").click()

if __name__ == "__main__":
    unittest.main()
