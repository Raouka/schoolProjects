# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

def nand(b1, b2):
    return not (b1 and b2)

def implies(b1, b2):
    if b1 == True and b2 == False:
        return False
    else:
        return True

def iff(b1, b2):
    if b1 == b2:
        return True
    else:
        return False

def xor(b1, b2):
    if b1 == b2:
        return False
    else:
        return True

print(nand(True, True))
print(nand(False, True))

print(implies(True, True))
print(implies(True, False))

print(iff(True, True))
print(iff(False, True))
print(xor(True, True))
print(xor(False, True))