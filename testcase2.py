#Test Case ID = ID_002
#Test Case Description: Fazer Cadastro com Campos em Branco
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
        #search_field = driver.find_element_by_id("user_email")
        #search_field.send_keys("email@email.com")
        driver.find_element_by_xpath("/html/body/div/div[2]/form/div[7]/div[2]/input").click()

if __name__ == "__main__":
    unittest.main()
