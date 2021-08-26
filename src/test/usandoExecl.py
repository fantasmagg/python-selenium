import unittest
from selenium.webdriver.common.keys import Keys

from src.functions.Functions import Functions as Selenium

class test_01(Selenium,unittest.TestCase):
    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.spotify.com/do/signup/", "CHROME")



    def test_001(self):
        NOMBRE= Selenium.leer_celda(self,"A1")
        APELLIDO=Selenium.leer_celda(self,"B1")
        DNI=Selenium.leer_celda(self,"C1")
       # Selenium.escribir_celda(self,"D1","HOLA DESDE QA")
        Selenium.crear_path(self)

    def tearDown(self):
       Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
