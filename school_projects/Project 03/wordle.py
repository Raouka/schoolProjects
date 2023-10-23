# Author   : Rayan Oukani
# Email    : roukani@umass.edu
# Spire ID : 34462508

import random

rList = ["WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"]

def get_guess():
    x = input("What word is this?: ")
    counter = 0
    end = ""
    while counter < 5:
        
        end = end + x[counter].upper()
        counter += 1
    return end

def print_word(streng):
    print(streng[0:1] + " " + streng[1:2] + " " + streng[2:3] + " " + streng[3:4] + " " + streng[4:5])
    
def exact_match_compare(solution, guess):
    
    returnee = ""
    
    for i in range(0, 5):
        if solution[i] == guess[i]:
            returnee+= "🟢"
        else:
            returnee+= "🔴"
    
    return returnee

def one_turn(solution):
    guess = get_guess()
    print_word(guess)
    print(exact_match_compare(solution, guess))
    if exact_match_compare(solution, guess) == "🟢🟢🟢🟢🟢":
        print("Congratulations")
        exit()
        
def make_solution():
    return rList[random.randint(0, len(rList)-1)]
        


soln = make_solution()
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
print(f"Word was \"{soln}\", better luck next time.")

