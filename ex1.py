"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime

uname = raw_input("What is your name: ")
uage = int(raw_input("what is your age: "))
howmany = int(raw_input("What's your favorite number: "))
curyear = datetime.datetime.now()
future = 100 - uage
#print future
#print curyear.year

print "Hello %s! You will be 100 years old in the year %s.\n" % (uname, future + curyear.year) * howmany
