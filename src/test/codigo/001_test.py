import unittest





class test_001(unittest.TestCase):
    def setUp(self):
        pass

    def test_001(self):
        self.variable_a = 50
        self.variable_b = 50
        self.resultado = self.variable_a+ self.variable_b

        self.assertEqual(self.variable_a,self.variable_b ,"los valores son diferentes")

        #self.assertTrue(self.resultado >=100,f"el valor es menor ")

    def test_002(self):
        self.variable_a = 5
        self.variable_b = 50
        self.resultado = self.variable_a + self.variable_b

        self.assertNotEqual(self.variable_a, self.variable_b, "los valores son iguales")

        # self.assertTrue(self.resultado >=100,f"el valor es menor ")

    def test_003(self):
        self.variable_a = 5
        self.variable_b = 50
        if self.variable_a < self.variable_b:
             self.resulta = True
        #assertTrue es para evaluar si una variable es true
        self.assertTrue(self.resulta, f"los valores son incorectos por la condicion {self.variable_a, self.variable_b}")

    def test_004(self):
        self.variable_a = "hola como estas estas bien como te trata la vida"
        self.variable_b = "trata"


        self.assertIn(self.variable_b, self.variable_a, "no esta")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
