import time

from selenium.webdriver.common.keys import Keys

from src.functions.Functions import Functions as Selenium
import unittest





class test_001(Selenium,unittest.TestCase):
    def setUp(self):
        #sabes que esa info se le pasa por el Functions ,pero en este caso la estamos sobre escribiendo
        #y pasandosela directamente
        Selenium.abrir_navegador(self,"https://www.spotify.com/do/signup/","CHROME")

    def test_001(self):

        #cargar el json
        Selenium.get_json_file(self,"Spotify_mensajedeError")
        #aqui se leen los valores que estan dentro del json llamados (entity)
        #Selenium.get_entity(self,"But sing")

        Selenium.get_elements(self,"But sing").send_keys("obedsilvestre339@gmail.com",Keys.ENTER)

        self.mensajeError = "Este correo electrónico ya está conectado a una cuenta. Inicia sesión."
        Selenium.espera_el_elemento(self,"Mensaje_de_error")
        assert Selenium.get_text(self,"Mensaje_de_error") == self.mensajeError ,"no son iguales"
        #self.driver.execute_script("document.write('hola');", Selenium.get_elements(self,"Mensaje_de_error"))

        Selenium.get_select_element(self,"select_month").select_by_visible_text("Enero")
        Selenium.scrol_js(self,"But sing")
        Selenium.click_js(self,"But sing")
        Selenium.esperar(self,2)

    def tearDown(self):
       Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
