"""
Python module that takes a list as arg and
returns the highest value in the list without 
using the max or min function
"""
def highest_score(scores):
    max_score = 0
    for score in scores:
        if score > max_score:
            max_score = score
    print(f"Highest value in the list is: {max_score}")
    return max_score

if __name__ == "__main__":
    highest_score([78,65,89,86,55,91,64,89])

# TODO: 1 PRINT