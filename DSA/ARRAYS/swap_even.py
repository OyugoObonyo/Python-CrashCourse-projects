"""
Module with a func that takes an array and waps even numbers to be at the beginning of array
"""
from traceback import print_tb
import unittest

def swap_even(array):
    """
    takes array and sorts it such that even numbers appear first
    @array: array passed
    Return: Array with even numbers appearing first
    """
    for i in range(len(array)-1):
        if array[i] % 2 != 0 and array[i+1] % 2 == 0:
            store = array[i]
            print(f"current number: {store}")
            array[i] = array[i+1]
            print(f"checking if {store} isn't even and {array[i+1]} is")
            array[i+1] = store
            print("check complete")
            print(f"current array: {array}")
    return array 

result = swap_even([1,2,4,5,8,6])
print(result)

"""
class TestCase(unittest.TestCase):
    def test_array_func(self):
        result = swap_even([1,2,4,5,8,6])
        expected = [2,4,8,6,1,5]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
"""