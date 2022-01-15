"""
Module that calculates the average height of 
a list of heights passed as args to it
rounded off to the nearest whole number
"""
def average_height(list):
    length = len(list)
    total_height = 0
    for l in list:
        total_height += l
    return (round(total_height/length))
    
if __name__ == "__main__":
    print(average_height([180, 124, 165, 173, 189, 169, 146]))