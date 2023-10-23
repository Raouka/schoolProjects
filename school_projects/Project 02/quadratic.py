# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

import math

def discriminant(a, b, c):
    return ((b**2) - (4*a*c))

def has_real_root(a, b, c):
    if discriminant(a, b, c) >= 0:
        return True
    else:
        return False
    
def get_real_root(a, b, c):
    assert(has_real_root(a,b,c))
    
    dis = (discriminant(a,b,c))
    
    
    r1 = (((-b) - (math.sqrt(dis))) / (2*a))
    r2 = (((-b) + (math.sqrt(dis))) / (2*a))
    
    return (r1, r2)
    
