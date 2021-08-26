# -*- codigo: uft-8 -*-
from src.functions.Functions import Functions as Selenium
from src.pages.practica import inicio as registro
import unittest
from selenium.webdriver.common.keys import Keys
import time




class test_001(Selenium,unittest.TestCase):
    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_001(self):
        Selenium.xpath_element(self,registro.de_Spoti_email).send_keys("obedsilvestre339@gmail.com",Keys.ENTER)
        self.mensaje = Selenium.xpath_element(self,registro.elmensaje)

        self.mensajeError ="Este correo electrónico ya está conectado a una cuenta. Inicia sesión."

        assert self.mensaje.text == self.mensajeError ,"no son iguales"
        self.driver.execute_script("alert('hola')")
        time.sleep(2)
        Selenium._xpath_element(self, registro.elmensaje)

        Selenium._id_element(self,registro.id_pass_entry)

    def tearDown(self):
       Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
