
from main import *
import unittest

class ExampleCase(unittest.TestCase):
    
        
    def test_case_1(self):
        
        self.assertEqual(seven(times(five())),35, "7*5=35")

    def test_case_2(self):

        self.assertEqual(four(plus(nine())), 13, "9+3=13")

    def test_case_3(self):

        self.assertEqual(eight(minus(three())), 5, "8%5=3")

    def test_case_4(self):

        self.assertEqual(six(divided_by(two())), 3, "6/2=3")

    def test_case_5(self):

        self.assertEqual(five(times(six(divided_by(two())))), 15, "5*6/2=15")
if __name__ == '__main__':
    unittest.main() 



