# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


uno = float(((-b) + math.sqrt((b**2) - (4 * a * c))) / (2 * a))
dos = float(((-b) - math.sqrt((b**2) - (4 * a * c))) / (2 * a))

print(f'Quadratic w/ variables {a, b, c} has roots: \n {uno} \n {dos}')