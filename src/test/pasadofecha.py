import time



from src.functions.Functions import Functions as Selenium
import unittest





class test_001(Selenium,unittest.TestCase):
    def setUp(self):
        #sabes que esa info se le pasa por el Functions ,pero en este caso la estamos sobre escribiendo
        #y pasandosela directamente
        Selenium.abrir_navegador(self,"https://www.google.com/","CHROME")
        #cargar el json
        Selenium.get_json_file(self,"Spotify_mensajedeError")

    def test_001(self):

       fecha = Selenium.textDateEnviaromenReploce(self,"today")
       Selenium.get_elements(self,"goog").send_keys(fecha)

       Selenium.esperar(self,2)

    def tearDown(self):
       Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
