import random
import math

def main():
    low = 1
    high = 100
    target = random.randint(low, high)
    num = input("Guess my number between 1 and 100: ")
    count = 0;
    while (target != num):
        count += 1
        if (num > target):
            num = input(str(num) + " is too high, try again: ")
        else:
            num = input(str(num) + " is too low, try again: ")

    print "It is " + str(num) + "! You got it! Average #of guesses is ~ " + str(math.log(high, 2)) + " guesses."
    congratext = ""    
    if (count < (math.log(high, 2) * 1.1)):
        congratext = "Excellent!"
    elif (count < (math.log(high, 2) * 1.5)):
        congratext = "Good job!"
    print "You took " + str(count) + " guesses. " + congratext

main()
