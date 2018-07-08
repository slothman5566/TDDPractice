import unittest
from main import  Solution

class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.testObject=Solution()   

    def test_case_1(self):
        input=[1,2,3,4,5]
        expect=4
        self.assertEqual(self.testObject.maxProfit(input),expect,'[1,2,3,4,5] should equal 4')
    
    def test_case_2(self):
        input=[3,3,5,0,0,3,1,4]
        expect=6
        self.assertEqual(self.testObject.maxProfit(input),expect,'[3,3,5,0,0,3,1,4] should equal 6')
    
    def test_case_3(self):
        input=[7,6,4,3,1]
        expect=0
        self.assertEqual(self.testObject.maxProfit(input),expect,'[7,6,4,3,1] should equal 0')
    
    def test_case_4(self):
        input=[]
        expect=0
        self.assertEqual(self.testObject.maxProfit(input),expect,'[] should equal 0')
        
    def test_case_5(self):
        input=[1,2,4,2,5,7,2,4,9,0]
        expect=13
        self.assertEqual(self.testObject.maxProfit(input),expect,'[1,2,4,2,5,7,2,4,9,0] should equal 13')
    
    def test_case_6(self):
        input=[1,2,4,2,5,7]
        expect=8
        self.assertEqual(self.testObject.maxProfit(input),expect,'[1,2,4,2,5,7] should equal 8')
    
    
    def test_case_7(self):
        input=[1,2,4,2,5,7,2,4,9,0,9]
        expect=17
        self.assertEqual(self.testObject.maxProfit(input),expect,'[1,2,4,2,5,7,2,4,9,0,9] should equal 17')
    
    def test_case_8(self):
        input= [1,3,5,4,3,7,6,9,2,4]
        expect=10
        self.assertEqual(self.testObject.maxProfit(input),expect,' [1,3,5,4,3,7,6,9,2,4] should equal 10')
    
    def test_case_9(self):
        input= [2,6,8,7,8,7,9,4,1,2,4,5,8]
        expect=14
        self.assertEqual(self.testObject.maxProfit(input),expect,'[2,6,8,7,8,7,9,4,1,2,4,5,8] should equal 14')
    
    def test_case_10(self):
        input= [5,2,3,0,3,5,6,8,1,5]
        expect=12
        self.assertEqual(self.testObject.maxProfit(input),expect,'[5,2,3,0,3,5,6,8,1,5] should equal 12')
   
    def test_case_11(self):
        input= [8,6,4,3,3,2,3,5,8,3,8,2,6]
        expect=11
        self.assertEqual(self.testObject.maxProfit(input),expect,'[8,6,4,3,3,2,3,5,8,3,8,2,6] should equal 11')
    
    
    def test_case_12(self):
        input= [3,4,6,0,3,7,5,8,2,9,1,6,6,2]
        expect=15
        self.assertEqual(self.testObject.maxProfit(input),expect,'[3,4,6,0,3,7,5,8,2,9,1,6,6,2] should equal 15')
   
if __name__ == '__main__':
    unittest.main() 