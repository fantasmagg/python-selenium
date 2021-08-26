import unittest
import allure
from src.functions.Functions import Functions as Selenium
#aqui es ya sabes todas las pruebas que tengan este feature se ejecutaran
@allure.feature(u'test 1')
#aqui es una brebe descripcion de la prueba
@allure.story(u'visitaremos spoti y aremos un shrechot')
@allure.testcase(u'prueba schechot',u'aqui va una url donde esten los pasos de esta prueba')
#aqui es el nivel de la prueba hay creo que 3 o 4
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u""" aqui va una brebe descripcion de los que vas hacer en la prueba <br/>""")

class MyTestCase(Selenium,unittest.TestCase):
    with allure.step(u'paso 1: entramos a spoti'):
        def setUp(self):
            Selenium.abrir_navegador(self, "https://www.spotify.com/do/signup/", "CHROME")

    def test_001(self):
        with allure.step(u'paso 2: creamos las carpetas donde se almacenaran las fotos .luego hacemos el schechot'):
            #Selenium.crear_path(self)
            Selenium.captura(self,'spoti')
            Selenium.esperar(self,3)


    def tearDown(self):
        with allure.step(u'paso 3 cerramos el driver'):
            Selenium.tearDown(self)
if __name__ == '__main__':
    unittest.main()
