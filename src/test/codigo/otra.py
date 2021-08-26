import unittest
import pytest

class test_001(unittest.TestCase):
    def setUp(self):
        pass

    def test_001(self):
        self.variable_a = 50
        self.variable_b = 50


        assert self.variable_a == self.variable_b ,"los valores son diferentes"

        #self.assertTrue(self.resultado >=100,f"el valor es menor ")

    def test_002(self):
        self.variable_a = 5
        self.variable_b = 50
        self.resultado = self.variable_a + self.variable_b


        #assert eso es con la libreria pytest
        assert  self.variable_a != self.variable_b, "los valores son iguales"

        # self.assertTrue(self.resultado >=100,f"el valor es menor ")

    def test_003(self):
        self.variable_a = 5
        self.variable_b = 50
        if self.variable_a < self.variable_b:
             self.resulta = True
        #assertTrue es para evaluar si una variable es true eso lo mismo assertTrue lo
        #unico es que aqui hay que
        assert self.resulta, f"los valores son incorectos por la condicion {self.variable_a, self.variable_b}"



    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
