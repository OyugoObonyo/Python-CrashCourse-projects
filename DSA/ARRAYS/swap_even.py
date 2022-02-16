"""
Module with a func that takes an array and waps even numbers to be at the beginning of array
"""
import unittest

'''
My algo
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
'''

"""
class TestCase(unittest.TestCase):
    def test_array_func(self):
        result = swap_even([1,2,4,5,8,6])
        expected = [2,4,8,6,1,5]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
"""

'''
SUMMARY: Algo shortcomings
Algo falls apart in the event of 2 successive odd numbers
In python, swapping can be done through assignment of the same line i.e a,b = b,a 
solution :
Start looping through and filling array values from the back,
compare first and last array value till you're back at the first value
def even_odd (A) :
    next_even, next-odd = 0, len(A) - I
    while next-even < next_odd:
        if A[next-even] % 2 == 0:
            next_even += 1
        else:
            A[next-even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
'''