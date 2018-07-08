import unittest
import main

class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.tester=main.Solution()
        
    def test_case_1(self):
        
        self.assertEqual(self.tester.josephus([1,2,3,4,5,6,7],3), [3, 6, 2, 7, 5, 1, 4], "[1,2,3,4,5,6,7] should equal [3, 6, 2, 7, 5, 1, 4]")

    def test_case_2(self):
        self.assertEqual(self.tester.josephus([1,2,3,4,5,6,7,8,9,10],1), [1,2,3,4,5,6,7,8,9,10], "[1,2,3,4,5,6,7,8,9,10] should equal [1,2,3,4,5,6,7,8,9,10]")

    def test_case_3(self):
        self.assertEqual(self.tester.josephus([1,2,3,4,5,6,7,8,9,10],2), [2, 4, 6, 8, 10, 3, 7, 1, 9, 5], "[1,2,3,4,5,6,7,8,9,10] should equal [2, 4, 6, 8, 10, 3, 7, 1, 9, 5]")

    def test_case_4(self):
        self.assertEqual(self.tester.josephus(["C","o","d","e","W","a","r","s"],4), ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'], "[C,o,d,e,W,a,r,s] should equal ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']")

    def test_case_5(self):
        self.assertEqual(self.tester.josephus([],3), [], "[] should equal []")

if __name__ == '__main__':
    unittest.main() 