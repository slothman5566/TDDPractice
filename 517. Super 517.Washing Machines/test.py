import unittest
import main

class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.tester=main.Solution()
        
    def test_case_1(self):
        
        self.assertEqual(self.tester.findMinMoves([0,2,0]), -1, "[0,2,0] can`t moving return -1")
    
    def test_case_2(self):
        
        self.assertEqual(self.tester.findMinMoves([1,0,5]), 3, "[1,0,5]  MinMoving is 3 ")
    
if __name__ == '__main__':
    unittest.main() 