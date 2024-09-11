import unittest
from src.calculator import add, substract, multiply, division

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        assert add(2, 3) == 5

    def test_substract(self):
        assert substract(10, 5) == 5

    def test_multiply(self):
        assert multiply(5, 2) == 10

    def test_division(self):
        assert division(10, 2) == 5

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)


