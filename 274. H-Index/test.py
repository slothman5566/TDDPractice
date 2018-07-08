import unittest
import main

class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.tester=main.Solution()
        
    def test_case_1(self):
        
        self.assertEqual(self.tester.hIndex([3,0,6,1,5]), 3, "[3,0,6,1,5] hIndex is 3")
    def test_case_2(self):
        
        self.assertEqual(self.tester.hIndex([100]), 1, "[100] hIndex is 1")
   
if __name__ == '__main__':
    unittest.main() 