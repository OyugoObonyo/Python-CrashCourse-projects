import unittest


def is_palindrome(arg):
    """
    is_palindrome- checks whether a given input is a palindrome i.e reads the same backwards and forwards 
    @arg: input to be checked
    Return: True if arg is palindrome false if not
    Assumptions:-
              also numbers are accepted inputs, provided they are positive numbers and greater than 10
              users won't enter floats
    """
    if isinstance(arg, int):
        if arg <= 10:
            print("Enter word or numbers greater thanm 10")
            return None
    arg = str(arg)
    arg_reverse = arg[::-1]
    if arg == arg_reverse:
        return True
    return False

class Test(unittest.TestCase):
    """
    Test case for plaindrome function
    """
    def test_suite(self):
        self.assertFalse(is_palindrome("Nurse"))
        self.assertFalse(is_palindrome(21))
        self.assertTrue(is_palindrome("madam"))
        self.assertIsNone(is_palindrome(0))

if __name__ == "__main__":
    unittest.main()


