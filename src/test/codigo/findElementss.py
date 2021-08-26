# -*- codigo: uft-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

 
class Test_004(unittest.TestCase):


    #datos del driver su funcionalidad
    def setUp(self):
        self.driver = webdriver.Chrome()
        #espera implicita
        self.driver.implicitly_wait(5)

        self.driver.maximize_window()

    #datos de la prueba
    def testName (self):
       self.driver.get("https://vehiculos.mercadolibre.com.do/")
       time.sleep(2)

       self.name = self.driver.find_elements(By.XPATH,"//*[contains (@class,'ui-search-item__title ui-search-item__group__element')]")



       self.lons = len(self.name)
       print(self.name)
       print(self.lons)

       self.cantidad = 0

       for self.lista in self.name:
           print(self.lista.text)
           self.cantidad+= 1
           print(self.cantidad)


    #CIERRE de la prueba
    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
