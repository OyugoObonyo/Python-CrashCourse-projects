"""
Learning Generators
"""

# basic generator syntax
'''
def factors(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k

factors_of_50 = factors(50)
for item in factors_of_50:
    print(item)
'''

# using a generator to store infine value
'''
def add_all_numbers():
    a, b = 0, 1
    while True:
        sum = a + b 
        a += 1
        b += 1
        yield sum

sum_everything = add_all_numbers()
print(sum_everything)
for item in sum_everything:
    print(item)
'''

#generator with multiple yield statements
'''
def factors(n):
    k=1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

factor_20 = factors(20)
for f in factor_20:
    print(f)
'''

'''
def ﬁbonacci( ):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
'''