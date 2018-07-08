import unittest
from main import  Solution

class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.testObject=Solution()   

    def test_case_1(self):
        input= "(()"
        target=2

        self.assertEqual(target,self.testObject.longestValidParentheses(input),"The longest valid parentheses substring is ()")
        
    def test_case_2(self):
        input= ")()())"
        target=4

        self.assertEqual(target,self.testObject.longestValidParentheses(input),"The longest valid parentheses substring is()()")
    def test_case_3(self):
        input= "()(()"
        target=2

        self.assertEqual(target,self.testObject.longestValidParentheses(input),"The longest valid parentheses substring is()")       
    def test_case_4(self):
        input=  ")()())()()("
        target=4

        self.assertEqual(target,self.testObject.longestValidParentheses(input),"The longest valid parentheses substring is ()()")     
    
   
if __name__ == '__main__':
    unittest.main() 