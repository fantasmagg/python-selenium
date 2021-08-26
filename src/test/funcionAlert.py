import unittest
from src.functions.Functions import Functions as Selenium

class test_alerta (Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self,"https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert","CHROME")
        Selenium.get_json_file(self,"alert")

    def test_Alert(self):
        Selenium.page_has_loaded(self)
        Selenium.switch_to_iframe(self,"FrameTRY")
        Selenium.get_elements(self, "Try itAler").click()
        Selenium.esperar(self, 4)
        Selenium.alert_windows(self, "accept")
        Selenium.esperar(self, 3)



    def tearDown(self):
        Selenium.tearDown(self)

if __name__ == '__main__':
    unittest.main()
