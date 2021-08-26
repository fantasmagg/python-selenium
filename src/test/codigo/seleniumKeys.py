# -*- codigo: uft-8 -*-
import time
import unittest
from selenium.webdriver.common.keys import Keys
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
       self.driver.get("https://www.google.com/")
       self.xpaths = "//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"
       self.driver.find_element(By.XPATH,self.xpaths).send_keys("que es la deprecion")
       time.sleep(2)
       self.driver.find_element(By.XPATH, self.xpaths).send_keys(Keys.BACK_SPACE ,Keys.BACK_SPACE)
       time.sleep(2)
       self.driver.find_element(By.XPATH, self.xpaths).send_keys(Keys.ARROW_DOWN)
       self.driver.find_element(By.XPATH,self.xpaths).send_keys(Keys.ARROW_DOWN)
       time.sleep(2)
       self.driver.find_element(By.XPATH, self.xpaths).send_keys(Keys.ENTER)
       time.sleep(2)

    #CIERRE de la prueba
    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
