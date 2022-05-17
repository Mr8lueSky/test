from factorial_function import factorial
from unittest import TestCase


class TestFactorialFunction(TestCase):
    def test_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_zero_number(self):
        self.assertEqual(factorial(0), 1)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_with_string(self):
        with self.assertRaises(ValueError):
            factorial("Some random string")
