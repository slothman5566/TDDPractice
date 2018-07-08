import unittest
import main

class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.tester=main.Solution()
        
    def test_case_1(self):
        
        self.assertEqual(self.tester.findDisappearedNumbers([4,3,2,7,8,2,3,1]), [5,6], "[4,3,2,7,8,2,3,1] missing [5,6]")
        
    def test_case_2(self):
        
        self.assertEqual(self.tester.findDisappearedNumbers([1,1]), [2], "[1,1] missing [2]")
    def test_case_3(self):
        
        self.assertEqual(self.tester.findDisappearedNumbers([]), [], "[] missing []")
    
   
if __name__ == '__main__':
    unittest.main() 