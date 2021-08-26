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
       self.driver.get("https://www.spotify.com/do/signup/")
       time.sleep(2)

       self.name = self.driver.find_elements(By.XPATH,'//*[contains (@class,"Label-jt4b9o-0 gENiDw")]')



       self.lons = len(self.name)
       print(self.name)
       print(self.lons)

       self.cantidad = 0

       for self.lista in self.name:
           RESULTADO_ESPERDADO =['¿Cuál es tu correo electrónico?','Confirma el correo electrónico','Crea una contraseña','¿Cómo quieres que te llamemos?','¿Cuál es tu fecha de nacimiento?','Día','Mes','Año']

           assert RESULTADO_ESPERDADO[self.cantidad] == self.lista.text,"no coinsiden"
           self.cantidad+= 1

    #CIERRE de la prueba
    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
