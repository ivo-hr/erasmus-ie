import math
import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate("5, 7, +"), 12)
        self.assertEqual(calculate("5, -7, +"), -2)
        self.assertEqual(calculate("5, 7, 8, +"), 20)
        self.assertEqual(calculate("5, 7, 8, 9, +"), 29)

    def test_subtract(self):
        self.assertEqual(calculate("5, 7, -"), -2)
        self.assertEqual(calculate("5, -7, -"), 12)
        self.assertEqual(calculate("5, 7, 8, -"), -2)
        self.assertEqual(calculate("5, 1, 8, 9, -"), 4)

    def test_multiply(self):
        self.assertEqual(calculate("5, 7, *"), 35)
        self.assertEqual(calculate("5, -7, *"), -35)
        self.assertEqual(calculate("5, 7, 8, *"), 280)
        self.assertEqual(calculate("5, 7, 8, 9, *"), 2520)
        

    def test_divide(self):
        self.assertEqual(calculate("5, 7, /"), 5/7)
        self.assertEqual(calculate("5, -7, /"), 5/-7)
        self.assertEqual(calculate("5, 7, 8, /"), 5/7)
        self.assertEqual(calculate("5, 0, /"), math.inf)
        self.assertEqual(calculate("-5, 0, /"), -math.inf)
        
        
if __name__ == '__main__':
    unittest.main()