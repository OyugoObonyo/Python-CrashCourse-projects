"""
Find count of digits in a number
"""
import unittest
from unittest import result


def count_digits(number):
    """
    count_digits - counts the number of digits in a number
    @number: number to be checked
    returns: number of digits or -1 if parameter is not an integer
    """
    if not isinstance(number, int):
        return -1
    number = str(number)
    return len(number)


class TestSuite(unittest.TestCase):
    """
    Test suite for the program
    """
    def test_normal_number(self):
        result = count_digits(679)
        self.assertEqual(result, 3)

    def test_single_number(self):
        result = count_digits(6)
        self.assertEqual(result, 1)

    def test_string(self):
        result = count_digits('679')
        self.assertEqual(result, -1)

    def test_list(self):
        result = count_digits([6, 7, 9])
        self.assertEqual(result, -1)

    def test_big_number(self):
        result = count_digits(123456789)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
