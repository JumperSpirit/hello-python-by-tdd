__author__ = 'amine'

import unittest;

class StringCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()
    def testCAlculateEmptyValue(self):
        self.assertEqual(self.calculator.calculate(''),0)
    def testCalculateSimpleNumber(self):
        self.assertEqual(self.calculator.calculate('1'),1)
    def testCalculateAdditionOfTowNumbers(self):
        self.assertEqual(self.calculator.calculate('1+2'),3)
    def testCalculateSoustracrionOfTowNumbers(self):
        self.assertEqual(self.calculator.calculate('1-2'),-1)
    def testCalculateMutipleOperations(self):
        self.assertEqual(self.calculator.calculate('10-2+7+6'),21)
class StringCalculator:
    def calculate(self,formule):
        result = 0
        if formule and formule != '' :
            number = ''
            index = 0
            operation = ''
        while index < len(formule)+1 :
                if index != len(formule) :
                    character = formule.__getitem__(index)
                    if character != '+' and character != '-':
                        number += character
                    elif character == '+' or character == '-' :
                        if operation =='+' or operation == '' : result += int(number)
                        if operation =='-' : result -= int(number)
                        number = ''
                        operation = character
                elif number != '' :
                    if operation =='+' or operation == '' : result += int(number)
                    if operation =='-' : result -= int(number)
                    number = ''
                index += 1
        return result

