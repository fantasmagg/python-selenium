import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.functions.inicializar import Inicializar
from selenium.webdriver.chrome.options import Options as OpcionesChrome

class Test_004(unittest.TestCase):


    #datos del driver su funcionalidad
    def setUp(self):
        self.driver = webdriver.Chrome(Inicializar.basedir+"\\drivers\\chromedriver.exe")
        #espera implicita
        self.driver.implicitly_wait(5)

        self.driver.maximize_window()

    #datos de la prueba
    def test_Name (self):
       self.driver.get("https://www.udemy.com/course/flask-framework-complete-course-for-beginners/?ranMID=39197&ranEAID=sIt9MIeGnaM&ranSiteID=sIt9MIeGnaM-wUPhqwZGQVf4R4SX7sr2sQ&LSNPUBID=sIt9MIeGnaM&utm_source=aff-campaign&utm_medium=udemyads&couponCode=70F4B5FDFF2D8499E285")
       #driver.find_element_by_xpath(  O  asi driver.find_element(By.Xpath,  para By from selenium.webdriver.common.by import  By
       eleme =self.driver.find_element_by_xpath("(//span[contains(.,'Gratis')])[1]").text
       print(eleme)
       time.sleep(30)

       #aqui le estamos dision mira vas a esperar que aparesca este elemento
       self.element = "//body/div[@id='__next']/main[1]/div[2]/div[1]/p[2]/span[1]/a[1]";
       try:
            wait = WebDriverWait(self.driver, 1)
            #visibility_of_element_located ) sabes que significa vdd
            wait.until(EC.visibility_of_element_located((By.XPATH, self.element)))
       except TimeoutException:
          self.skipTest("nose encontro el element")

       self.name = self.driver.find_elements(By.XPATH,'//*[contains (@class,"Input-sc-1698ofb-0 efgBiC")]')

       self.lons = len(self.name)
       print(self.lons)

       self.cantidad = 0

       for self.lista in self.name:
           print(self.lista)
           self.cantidad += 1
           print(self.cantidad)







    #CIERRE de la prueba
    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
