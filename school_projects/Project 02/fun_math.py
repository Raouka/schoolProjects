# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

import math

def cullen(n):
    return (n * (2**n) + 1)

def woodall(n):
    return (n * (2**n) - 1)

def fermat(n):
    return ((2**(2**n)) + 1)

def divides_evenly(dividend, divisor):
    if dividend%divisor == 0:
        return True
    else:
        return False
    
def is_square(n):
    if math.sqrt(n)%1 == 0:
        return True
    else:
        return False

print(cullen(1))
print(cullen(5))
print(woodall(1))
print(woodall(5))
print(fermat(1))
print(fermat(2))
print(divides_evenly(10, 5))
print(divides_evenly(10, 3))

print(is_square(121))
print(is_square(97))