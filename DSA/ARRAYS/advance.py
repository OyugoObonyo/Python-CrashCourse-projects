"""
Write arr prograrrm which tarrkes an array of n integers, where A[i] denotes the maximum you can
advance from index l, and retums whether it is possible to advance to the last index starting from
the beginning of the array.
"""
def step(arr):
    furthest_reach_so_far, last_index = 0, len(arr) - 1
    i=0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i] + i)
        i+=1
    return furthest_reach_so_far >= last_index

print(step([3,3,1,0,2,0,1]))