import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import Select
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
        #driver.find_element_by_xpath(  O  asi driver.find_element(By.Xpath,  para By from selenium.webdriver.common.by import  By
        self.driver.find_element_by_xpath("((//body/div[@id='__next'])//*[contains (@type,'email')])[1]").click()
        self.driver.find_element(By.XPATH,"((//body/div[@id='__next'])//*[contains (@type,'email')])[1]").send_keys("obed")
        time.sleep(10)

        #select
        selector =Select (self.driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div/form/div[5]/div[2]/div[2]/div/div[2]/select"))
        selector.select_by_visible_text("Enero")
        #

        #xpath del text comparando texto
        texto= self.driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/h2").text

        print(texto)

        assert texto == "Regístrate gratis para escuchar" , "no son iguales"
        #--------------------------------------------------------------------

    #CIERRE de la prueba
    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
