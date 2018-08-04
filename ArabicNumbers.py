__author__ = 'amine'

import unittest;

class ArabicNumberMapperTest(unittest.TestCase):
    def setUp(self):
        self.arabicNumberMapper = ArabicNumberMapper()

    def testMapSimpleNumber(self):
        self.assertEqual(self.arabicNumberMapper.map(1),'I')

    def testMapAnOtherSimpleNumber(self):
        self.assertEqual(self.arabicNumberMapper.map(5),'V')

    def testMapAnOtherSimpleNumberInTheSameRange(self):
        self.assertEqual(self.arabicNumberMapper.map(4),'IV')

    def testMapComplexSmallNumber(self):
        self.assertEqual(self.arabicNumberMapper.map(3),'III')

class ArabicNumberMapper:
    def __init__(self):
        self.arabicNumbersDictionary = {1:'I',5:'V',4:'IV'}
        self.listOfSortedRomainNumbers = list(
            reversed(
                sorted(
                    self.arabicNumbersDictionary.keys()
                )
            )
        )

    def __mapSimpleNRomainNumber(self):
        arabicNumber = ''
        for romainNumber in self.listOfSortedRomainNumbers:
            if romainNumber <= self.number :
                arabicNumber += self.arabicNumbersDictionary.get(romainNumber)
                self.number -= romainNumber
        return arabicNumber

    def map(self,number):
        self.number = number
        arabicNumber = self.__mapSimpleNRomainNumber()
        if self.number == 0:
            return arabicNumber
        return arabicNumber + self.map(self.number)



