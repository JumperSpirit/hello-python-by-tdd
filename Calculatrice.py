import unittest;

class CalculatriceTestsclass(unittest.TestCase):
    def setUp(self):
        self.calculatrice = Calculatrice()

    def testAddition(self):
        self.assertEqual(4,self.calculatrice.addition(2,2))

    def testSoustraction(self):
        self.assertEqual(1,self.calculatrice.soustraction(2,1))

class Calculatrice :
     def addition(self,a,b):
         return a+b
     def soustraction(self,a,b):
         return a-b

