import unittest
from app import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertIsNone(calculator.divide(10, 0))

if __name__ == '__main__':
    unittest.main()
