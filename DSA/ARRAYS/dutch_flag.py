"""
Write a program that takes an array A and an index into A, and rearranges the elements such
that all elements less than the "pivot" appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.
"""
def rearrange_array(array, pivot):
    if len(array) <= 1:
        return array
    number = array.pop(pivot)
    less_than = []
    equal_to = []
    greater_than = []
    for item in array:
        if item < number:
            less_than.append(item)
        elif item == number:
            equal_to.append(item)
        else:
            greater_than.append(item)
    return less_than + equal_to + [number] + greater_than

print(rearrange_array([0,1,2,0,2,1,1], 3))