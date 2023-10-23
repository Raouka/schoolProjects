# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

n = int(input("Enter a number: "))
i = 1         
sm = 0

while i<=n:   
  sm += 1/(i**2)
  i += 1 
  
print(f'sum: {sm}')
print(f'approximate value of pi is: {(6*sm)**.5}')