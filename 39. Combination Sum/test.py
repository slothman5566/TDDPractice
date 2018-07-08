import unittest
from main import  Solution

class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.testObject=Solution()   

    def test_case_1(self):
        input=[]
        target=5
        ans=[]
        self.assertEqual(ans,self.testObject.solution(input,target),"input empty list")
        
    def test_case_2(self):
        input=[1,2]
        target=3
        ans=[[1,1,1],[1,2]]

        self.assertEqual(ans,self.testObject.solution(input,target),"simple test")
    
    def test_case_3(self):
        input=[2,3]
        target=1
        ans=[]
        self.assertEqual(ans,self.testObject.solution(input,target),"target is minor than input")
    
    def test_case_4(self):
        input=[1,1,2]
        target=3
        ans=[[1,1,1],[1,2]]
        self.assertEqual(ans,self.testObject.solution(input,target),"input have duplicata element")
    
    
if __name__ == '__main__':
    unittest.main() 