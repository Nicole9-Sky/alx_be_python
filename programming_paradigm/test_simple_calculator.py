import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(3, 2), 5)
        
        # Add more assertions to thoroughly test the add method.
        
    def tes_subtraction(self):
        """Test the subtraction method.""" 
        self.assertEqual(self.calc.subtract(5, 3), 2)   
        self.assertEqual(self.calc.subtract(1, 1), 0)   
        self.assertEqual(self.calc.subtract(-5, 3), -8)   
        self.assertEqual(self.calc.subtract(6, 2), 4)  
        
    def test_multiplication(self):
        """test_multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(4, 1), 4)
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(1, 0), 0)
        
    def test_division(self):
        """test_division method."""
        self.assertEqual(self.calc.divide(6, 2), 3)    
        self.assertEqual(self.calc.divide(4, 2), 2)    
        self.assertEqual(self.calc.divide(-6, 2), -3)    
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)   
        
        
        self.assertIsNone(self.calc.divide(5, 0), 0) 
        self.assertIsNone(self.calc.divide(0, 0), 0) 
        
        if __name__ == "__main__":
            unittest.main()
    
