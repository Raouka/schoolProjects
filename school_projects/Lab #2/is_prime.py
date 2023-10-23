# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

def is_prime(n):
    checker = int(n**.5)
    i = 2       
    while i<=checker:  
        if n%i == 0 or n%checker == 0:
            return False
        i += 1     
    return True



print(is_prime(15))     
print(is_prime(17))    
print(is_prime(25))      
print(is_prime(26))     
print(is_prime(97))     
print(is_prime(21))     
