# Test Case ID = ID_0011
# Test Case Description: Adicionar "Experiência" com dados invalidos ou em branco.
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
        search_field.send_keys("mariasantostestes@gmail.com")
        # search_field.submit()
        search_field2 = driver.find_element_by_id("user_password")
        search_field2.send_keys("testes123456")
        # search_field2.submit()
        driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div[2]/input").click()
        driver.find_element_by_xpath("/html/body/div/div[2]/section/div/div/div[6]/div[1]/div/a").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/form/div[2]/button").click()

if __name__ == "__main__":
    unittest.main()
