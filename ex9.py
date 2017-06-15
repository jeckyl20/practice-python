# vim: set fileencoding=utf_8 :
'''
Guessing Game One   
Exercise 9 (and Solution)

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.

'''
#from random import *
import random
total = 0
play = ""

## Function to check if users guess is the random number and keep asking until it is correct. Also keep track of number of guesses.
def check(uguess, num):
    global total
#    print "You have guessed %d times." % total
    while uguess != num:
        ans = 0
        if uguess > num:
            print "You guessed too high."
            ans += 1
        elif uguess < num:
            print "You guessed too low."
            ans += 1
        else:
            print "That is correct!"
            ans = 0
#        print "Variable ans is: %d" % ans
        uguess = int(raw_input("Please choose another numnber from 1 to 9: "))
        total += 1
    return ans

while play != "exit":
    total
## Different ways of using randint from random module, depends on how it was imported.
#    rnum = randint(1, 9)
    rnum = random.randint(1, 9)
    guess = int(raw_input("Please choose a number from 1 to 9: "))
    total += 1
#    print "Random number is: %d" % rnum
#    print "Your guess was: %d" % guess
    check(guess, rnum)
#    print "Total guesses: %d" % total
    play = raw_input("Would you like to play again? Type 'exit' to quit: ")

print "You took %d guesses." % total
