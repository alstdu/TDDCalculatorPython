import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_two_numbers(self):
        result = self.calc.add(4, 2)
        self.assertEqual(result, 6)
        
    def test_subtract_two_numbers(self):
        result = self.calc.subtract(4, 2)
        self.assertEqual(result, 2)
        
    def test_multiply_two_numbers(self):
        result = self.calc.multiply(4, 2)
        self.assertEqual(result, 8)
    
    def test_divide_two_numbers(self):
        result = self.calc.divide(4, 2)
        self.assertEqual(result, 2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(4, 0)
            
    def test_divide_decimal_result(self):
        result = self.calc.divide(5, 2)
        self.assertEqual(result, 2.5)
        
    def test_divide_large_numbers(self):
        result = self.calc.divide(1000000, 2)
        self.assertEqual(result, 500000)
        
    def test_divide_negative_numbers(self):
        result = self.calc.divide(-10, 2)
        self.assertEqual(result, -5)
        
    def test_divide_both_negative_numbers(self):
        result = self.calc.divide(-10, -2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
