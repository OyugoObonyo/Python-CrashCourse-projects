"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the minimum number of times the original sorted list was rotated,
to obtain the given list. Your function should have the worst-case complexity of O(log N),
where N is the length of the list. You can assume that all the numbers in the list are unique.

The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
"""
import unittest


# Apply brute-force solution here
'''
def count_rotations(arr):
    position = 1
    limit = len(arr) - 1
    while position <= limit:
        if arr[position] < arr[position-1]:
            return position
        else:
            position += 1
    return 0
'''

def count_rotations(nums):
 
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)
 
    # loop till the search space is exhausted
    while left <= right:
 
        # if the search space is already sorted, we have
        # found the minimum element (at index `left`)
        if nums[left] <= nums[right]:
            return left
 
        mid = (left + right) // 2
 
        # find the next and previous element of the `mid` element (in circular manner)
        next = (mid + 1) % len(nums)
        prev = (mid - 1 + len(nums)) % len(nums)
 
        # if the `mid` element is less than both its next and previous
        # neighbor, it is the list's minimum element
 
        if nums[mid] <= nums[next] and nums[mid] <= nums[prev]:
            return mid
 
        # if nums[mid…right] is sorted, and `mid` is not the minimum element,
        # then the pivot element cannot be present in nums[mid…right],
        # discard nums[mid…right] and search in the left half
 
        elif nums[mid] <= nums[right]:
            right = mid - 1
 
        # if nums[left…mid] is sorted, then the pivot element cannot be present in it;
        # discard nums[left…mid] and search in the right half
 
        elif nums[mid] >= nums[left]:
            left = mid + 1
 
    # invalid input
    return -1
 

'''
def count_rotations(array):
    start = 0
    end = len(array) - 1
    while start <= end:
        # Check if list is already sorted
        if array[start] <= array[end]:
            return 0
        middle = start + end // 2
        # find elements before and after middle element
        after = (middle + 1) % len(array)
        before = (middle - 1) % len(array)
        if array[middle] < array[before]:
            return middle
        elif array[middle] <= array[end]:
            end = middle - 1
        elif array[middle] >= array[start]:
            start = middle + 1
    return -1
'''
# print(count_rotations([[19, 20, 22, 25, 30, 39, 40, 11]]))


class TestCase(unittest.TestCase):
    def test_rotations(self):
        result = count_rotations([5, 6, 9, 0, 2, 3, 4])
        expected_result = 3
        self.assertEqual(result, expected_result)

    def test_rotations_list_of_ten(self):
        result = count_rotations([19, 25, 29, 3, 5, 6, 7, 9, 11, 14])
        expected_result = 3
        self.assertEqual(result, expected_result)

    def test_rotated_five_times(self):
        result = count_rotations([19, 20, 22, 25, 30, 9, 10, 11])
        expected_result = 5
        self.assertEqual(result, expected_result)

    def test_rotate_one_element(self):
        result = count_rotations([2])
        expected_result = 0
        self.assertEqual(result, expected_result)
    
    def test_not_rotated(self):
        result = count_rotations([3,5,7,9])
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        result = count_rotations([])
        expected_result = -1
        self.assertEqual(result, expected_result)
    
    def test_rotate_one_less(self):
        """
        testing to check a case where a list is rotated n-1 times
        """
        result = count_rotations([19, 20, 22, 25, 30, 39, 40, 11])
        expected_result = 7
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()


    
   
