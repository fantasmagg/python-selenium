import unittest

class test_001(unittest.TestCase):
    def set(self):
        pass

    def test_001(self):
        self.variable_a = 50
        self.variable_b = 50
        self.resultado = self.variable_a+ self.variable_b

        self.assertTrue(self.resultado >=100,f"el valor es menor ")

if __name__ == '__main__':
    unittest.main()