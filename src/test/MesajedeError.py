# -*- codigo: uft-8 -*-
import time
import unittest

import pytest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.practica import inicio as spotiXpaths
from src.functions.Functions import Functions as Selenium

 
class Test_004(unittest.TestCase):


    #datos del driver su funcionalidad
    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.spotify.com/do/signup/", "CHROME")
        Selenium.get_json_file(self,"Spotify_mensajedeError")

    #datos de la prueba
    def testName (self):
       self.driver.get("https://www.spotify.com/do/signup/")
       time.sleep(1)

       Selenium.get_elements(self,"But sing").send_keys("obedsilvestre16@gmail.com",Keys.ENTER)
       time.sleep(1)




       Selenium.assert_text(self,"mesaERROR","Este correo electrónico ya está conectado a una cuenta. Inicia sesión.")
       verifica =   Selenium.check_text(self,"mesaERROR")

       if  verifica:
           pytest.skip("error")
           unittest.TestCase.skipTest("e; email ya existes")
          #OJO el clear no funciona en el cuadro de email
           Selenium.send_key_text(self,"But sing","sssssssss16@gmail.com")



    #CIERRE de la prueba
    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
