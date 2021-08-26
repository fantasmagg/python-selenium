import time

from selenium.webdriver.common.keys import Keys

from src.functions.Functions import Functions as Selenium
import unittest


class   Test_database(Selenium,unittest.TestCase):
    def setUp(self):
        # sabes que esa info se le pasa por el Functions ,pero en este caso la estamos sobre escribiendo
        # y pasandosela directamente
        Selenium.abrir_navegador(self, "https://www.spotify.com/do/signup/", "CHROME")


    def test_001(self):
        Selenium.get_json_file(self, "Spotify_mensajedeError")

        Selenium.get_elements(self, "But sing").send_keys("obedsilvestre339@gmail.com", Keys.ENTER)

        dato=Selenium.get_text(self,"Mensaje_de_error")

        #-----------------------base de datos
        Selenium.insertarValores(dato)
        Selenium.databaseSelect()
        Selenium.cerrarConesion()



    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
