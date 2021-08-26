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
        self.driver.get("https://www.spotify.com/do/signup/")
        self.driver.maximize_window()
    #datos de la prueba
    def testName (self):

        #driver.find_element_by_xpath(  O  asi driver.find_element(By.Xpath,  para By from selenium.webdriver.common.by import  By
       self.enlase = self.driver.find_element_by_xpath("//body/div[@id='__next']/main[1]/div[2]/div[1]/p[2]/span[1]/a[1]")
       self.enlase.click()
       print("ventanas" + str(self.driver.window_handles))
       #self.driver.back()
       self.driver.switch_to.window(self.driver.window_handles[0])
       time.sleep(2)

    #CIERRE de la prueba
    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
