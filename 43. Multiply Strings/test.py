import unittest
from main import  Solution

class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.testObject=Solution()   

    def test_case_1(self):
        num1 = "2"
        num2 = "3"
        ans='6'
        self.assertEqual(ans,self.testObject.multiply(num1,num2),"2*3=6")
        

if __name__ == '__main__':
    unittest.main() 