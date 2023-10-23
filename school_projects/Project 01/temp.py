# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

inf = float(input("Enter temperature in Fahrenheit: "))

inc = ((inf - 32) * (5 / 9))
ink = inc + 273.15


print(f'{inf} degrees Fahrenheit is equal to: \n {inc} degrees Celsius \n {ink} degrees Kelvin')