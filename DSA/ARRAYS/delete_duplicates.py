"""
Write a program which takes as input a sorted array and updates it so that all duplicates have been
removed and the remaining elements have been shifted left to fill the emptied indices. Return the
number of valid elements. Many languages have library functions for performing this operation-
you cannot use these functions.
"""
def remove_duplicate(array):
    """
    remove_duplicate - removes duplicate from array
    @array: sorted array duplicates ought to be removed from
    Return: New array
    """
    size = len(array)
    write_index = 1
    for i in range(1, size):
        if array[write_index - 1] != array[i]:
            array[write_index] = array[i]
            write_index += 1
    return array
     
print(remove_duplicate([2,3,5,5,7,11,11,11,13]))
            