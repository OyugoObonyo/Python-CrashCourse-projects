"""
Module that sums up all even numbers between 1 and 100<including 100>
"""
def sum_even():
    sum = 0
    for i in range(2, 101, 2):
        sum += i
    print(sum)

if __name__ == '__main__':
    sum_even()