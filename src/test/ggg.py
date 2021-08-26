import time

from selenium.webdriver.common.keys import Keys

from src.functions.Functions import Functions as Selenium
import unittest





class test_001(Selenium,unittest.TestCase):
    def setUp(self):
        #sabes que esa info se le pasa por el Functions ,pero en este caso la estamos sobre escribiendo
        #y pasandosela directamente
        Selenium.abrir_navegador(self,"https://www.google.com/","CHROME")

    def test_001(self):

        #cargar el json
        Selenium.get_json_file(self,"Spotify_mensajedeError")
        #aqui se leen los valores que estan dentro del json llamados (entity)

        Selenium.get_elements(self,"goog").send_keys("obedsilvestre339@gmail.com")


        Selenium.get_elements(self, "goog").clear()
        Selenium.get_elements(self,"goog").send_keys("hola")

        Selenium.esperar(self)

    def tearDown(self):
       Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
