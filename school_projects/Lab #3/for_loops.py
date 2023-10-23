# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

def count_strings(array, n):  # detect how many strings have n amount of characters    
    count = 0
    
    for string in array:
        if len(string) >= n:
            count = count + 1
    return count        


def get_factors(n):
    factors = []
    
    for i in range(2, n//2+1):
        if n%i == 0:
            factors.append(i)
    
    return factors

def get_names(first_names, last_names):
    full_names = []
    
    for name in first_names:
        for lname in last_names:
            full_names.append(f'{name} {lname}')
    print(full_names)
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
 
get_names(first_names, last_names)

count_strings(['', 'a', 'aa', 'aaa'], 0)   # should return 4
count_strings(['', 'a', 'aa', 'aaa'], 2)   # should return 2 
count_strings(['', 'a', 'aa', 'aaa'], 4)   # should return 0

get_factors(10)            # should return [2, 5]
get_factors(12)            # should return [2, 3, 4, 6]
get_factors(16)            # should return [2, 4, 8]
get_factors(17)            # should return an empty list []
