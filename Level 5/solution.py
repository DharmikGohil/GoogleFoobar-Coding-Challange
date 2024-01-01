#  necessary functions and modules
from math import factorial
from collections import Counter
from fractions import gcd

# Function to calculate the cycle count
def cycle_count(c, n):
    cc = factorial(n)
    
    # Iterate through the Counter items and adjust the cycle count
    for a, b in Counter(c).items():
        cc //= (a ** b) * factorial(b)
    return cc

#  Generator function to generate cycle partitions

def cycle_partitions(n, i=1):
    yield [n]
    
    # Iterate through possible cycle sizes
    for i in range(i, n // 2 + 1):
        
        # Recursively generate cycle partitions
        for p in cycle_partitions(n - i, i):
            yield [i] + p

# Main solution function
def solution(w, h, s):    
    grid = 0
    # Iterate through cycle partitions for both width and height
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):            
            # Calculate the contribution of each configuration
            m = cycle_count(cpw, w) * cycle_count(cph, h)
            grid += m * (s ** sum([sum([gcd(i, j) for i in cpw]) for j in cph]))

    # Return the result as a decimal string
    return str(grid // (factorial(w) * factorial(h)))
