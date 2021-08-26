# -*- codigo: uft-8 -*-
import time
import unittest
from src.functions.Functions import Functions as Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains as actichen

 
class Test_004(unittest.TestCase):


    #datos del driver su funcionalidad
    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.spotify.com/do/signup/", "CHROME")


    #datos de la prueba
    def testName (self):
       self.driver.get("https://www.amazon.com/")

       time.sleep(3)
       local = self.driver.find_element(By.XPATH,"//span[contains(text(),'Inicio de Página')]")
       self.driver.execute_script("arguments[0].scrollIntoView();",local)
       time.sleep(2)
       localclick = self.driver.find_element(By.XPATH, '// *[ @ id = "navFooter"] / div[1] / div / div[1] / ul / li[1] / a')
       self.driver.execute_script("arguments[0].click();",localclick)


       time.sleep(5)


    #CIERRE de la prueba
    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
