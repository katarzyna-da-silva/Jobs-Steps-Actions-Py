# test_functions.py

import unittest
from functions import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7)

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -5)
        self.assertEqual(result, -7)

    def test_add_mixed_numbers(self):
        result = add_numbers(10, -3)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()