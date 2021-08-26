import time

from selenium.webdriver.common.keys import Keys

from src.functions.Functions import Functions as Selenium
import unittest





class test_001(Selenium,unittest.TestCase):
    def setUp(self):
        #sabes que esa info se le pasa por el Functions ,pero en este caso la estamos sobre escribiendo
        #y pasandosela directamente
        Selenium.abrir_navegador(self,"https://www.spotify.com/do/signup/","CHROME")
        #cargar el json
        Selenium.get_json_file(self,"Spotify_mensajedeError")

    def test_001(self):
        Selenium.save_variable_ecenario(self,"yatienesunacuenta","yatengo una cuenta")

        Selenium.new_window(self,"https://www.spotify.com/do/signup/")
        Selenium.switch_to_windows_name(self,"spoti")

        Selenium.espera_el_elemento(self,"yatienesunacuenta")
        #aqui estamos comprobando si el texto es igual a la pagina principal
        #"yatengo una cuenta" ese es el valor que guadamos de la primera pagina y ahora lo estamos coparanod con la segunda
        #que tengan el mismo texto
        Selenium.compare_with_variable(self,"yatienesunacuenta","yatengo una cuenta")



    def tearDown(self):
       Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
