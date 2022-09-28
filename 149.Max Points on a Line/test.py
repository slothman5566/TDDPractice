import unittest
import main


class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.testObject=main.Solution()
        
    def test_case_1(self):
        input=[ ]
        ans=0
       
        self.assertEqual(ans,self.testObject.maxPoints(input),"input have zero point")
    
    def test_case_2(self):
        input=[main.Point()]
        ans=1
        self.assertEqual(ans,self.testObject.maxPoints(input),"input have one point")

    def test_case_3(self):
        input=[main.Point(),main.Point()]
        ans=2
        self.assertEqual(ans,self.testObject.maxPoints(input),"input have two same points")
    
    def test_case_4(self):
        input=[main.Point(),main.Point(0,1)]
        ans=2
        self.assertEqual(ans,self.testObject.maxPoints(input),"input have two different points")
    
    def test_case_5(self):
        input=[main.Point(),main.Point(),main.Point()]
        ans=3
        self.assertEqual(ans,self.testObject.maxPoints(input),"input have three same points")
        
    def test_case_6(self):
        input=[main.Point(),main.Point(),main.Point(1,1)]
        ans=3
        self.assertEqual(ans,self.testObject.maxPoints(input),"input one of three is different points")
        
    def test_case_7(self):
        input=[main.Point(),main.Point(0,1),main.Point(1,1)]
        ans=2
        self.assertEqual(ans,self.testObject.maxPoints(input),"input have three different points")
    def test_case_8(self):
        input=[main.Point(),main.Point(0,1),main.Point(1,1)]
        ans=2
        self.assertEqual(ans,self.testObject.maxPoints(input),"input have inf slope")
    
    def test_case_9(self):
        input=[main.Point(),main.Point(94911151,94911150),main.Point(94911152,94911151)]
        
        ans=2
        self.assertEqual(ans,self.testObject.maxPoints(input),"input have to Accurate calculation  ")   
if __name__ == '__main__':
    unittest.main() 