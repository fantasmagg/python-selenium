import time
import unittest
from src.functions.Functions import Functions as Selenium
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import Select
class Test_005(unittest.TestCase):
    def setUp(self):
        Selenium.abrir_navegador(self,"https://www.amazon.com/","CHROME")


    def test_frame(self):

        Selenium.new_window(self,"https://www.amazon.com/-/es/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice_2bf4fe8c5ec54e6bae2d1c24043f012b")
        time.sleep(2)
        #aqui pasamos entre ventanas
        #Selenium.switch_to_windows_name(self,"segunda")
        Selenium.switch_to_windows_name(self,"Principal")
        time.sleep(2)
        Selenium.switch_to_windows_name(self, "segunda")

        time.sleep(2)





    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
