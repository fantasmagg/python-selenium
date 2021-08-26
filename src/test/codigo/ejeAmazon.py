# -*- codigo: uft-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains as actichen

 
class Test_004(unittest.TestCase):


    #datos del driver su funcionalidad
    def setUp(self):
        self.driver = webdriver.Chrome()
        #espera implicita
        self.driver.implicitly_wait(5)

        self.driver.maximize_window()

    #datos de la prueba
    def testName (self):
       self.driver.get("https://www.amazon.com/")
       time.sleep(2)

       local = self.driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']")
       action = actichen(self.driver)
       action.move_to_element(local)
       action.perform()


       #click a cuenta dentro de la cosa esa que se desplasa
       localClick =self.driver.find_element_by_xpath('//*[@id="nav-al-your-account"]/a[1]')
       localClick.click()
       time.sleep(2)


    #CIERRE de la prueba
    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
