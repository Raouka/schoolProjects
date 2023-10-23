# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508


first = int(input("What is the dividend: "))
second = int(input("What is the divisor: "))

real = first // second
unreal = first % second

print(f'{first}/{second} equals:\n\t{real} and {unreal}/{second}')