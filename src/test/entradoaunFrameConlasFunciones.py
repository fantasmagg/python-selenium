import time
import unittest
from src.functions.Functions import Functions as Selenium
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import Select
class Test_005(unittest.TestCase):
    def setUp(self):
        Selenium.abrir_navegador(self,"https://chercher.tech/practice/frames-example-selenium-webdriver","CHROME")


    def test_frame(self):
        Selenium.get_json_file(self,"frame")

        Selenium.switch_to_iframe(self,"frameUno")

        Selenium.send_key_text(self,"Topic_entry","hola")
        Selenium.switch_to_iframe(self,"frameTres")
        Selenium.get_elements(self,"CheckBox").click()
        Selenium.switch_to_parent_frame(self)  # saliendo del frame 3
        Selenium.switch_to_parent_frame(self)  # saliendo del frame 1

        Selenium.switch_to_iframe(self,"frameDos")
        Selenium.selector_text(self,"selector_animals","Avatar")
        Selenium.switch_to_parent_frame(self)

        #comprobando titulo
        title="Frames Examples in Selenium Webdriver"
        assert Selenium.get_text(self,"Title_frames_examples") == title ,"no son iguales"

        time.sleep(2)





    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
