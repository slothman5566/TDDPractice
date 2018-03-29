import unittest
import main

class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.testObject=main.Calculator()
        
    def test_case_1(self):
        input=''
        ans=0
        self.assertEqual(self.testObject.calc(input), 0, "Should work with empty string")
    def test_case_2(self):
        self.assertEqual(self.testObject.calc("1 2 3"), 3, "Should parse numbers")
    def test_case_3(self):
        self.assertEqual(self.testObject.calc("1 2 3.5"), 3.5, "Should parse float numbers")
    def test_case_4(self):
        self.assertEqual(self.testObject.calc("1 3 +"), 4, "Should support addition")
    def test_case_5(self):
        self.assertEqual(self.testObject.calc("1 3 *"), 3, "Should support multiplication")
    def test_case_6(self):
        self.assertEqual(self.testObject.calc("1 3 -"), -2, "Should support subtraction")
    def test_case_7(self):
        self.assertEqual(self.testObject.calc("4 2 /"), 2, "Should support division")
    def test_case_8(self):
        self.assertEqual(self.testObject.calc("4 0 /"), 'division by zero', "Should handle division zero")


if __name__ == '__main__':
    unittest.main() 