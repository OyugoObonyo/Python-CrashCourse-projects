"""
Find the largest digit
"""
import unittest


def largest_digit(number):
    """
    largest_digit - Finds largest digit in a number
    @number: number to be checked
    returns: largest digit in a number or -1 if parameter not a number 
    """
    if not isinstance(number, int):
        return -1
    # make integer iterable
    number = str(number)
    largest_num = 0
    i = 0
    if len(number) == 1:
        return int(number)
    while i < len(number):
        # maximum value in a digit can be 9
        if number[i] == '9':
            return 9
        if number[i] > number[i + 1]:
            largest_num = number[i]
        i += 1
    return int(largest_num)


class TestSuite(unittest.TestCase):
    """
    The function's test suite
    """
    def test_normal_number(self):
        result = largest_digit(679)
        self.assertEqual(result, 9)

    def test_single_number(self):
        result = largest_digit(6)
        self.assertEqual(result, 6)

    def test_string(self):
        result = largest_digit('679')
        self.assertEqual(result, -1)

    def test_list(self):
        result = largest_digit([6, 7, 9])
        self.assertEqual(result, -1)

    def test_big_number(self):
        result = largest_digit(123459789)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
