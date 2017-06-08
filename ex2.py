'''
Odd Or Even 
input if types int equality comparison numbers mod
Again, the exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Exercise 2 (and Solution)

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

unum = int(raw_input("Please give me a number: "))

if unum % 4 == 0:
    print "%d is divisible by 4, interesting." % unum
elif unum % 2 == 0:
    print "%d is an even number." % unum
else:
    print "%d is an odd number." % unum


print "Let's do something with more numbers now."
num = int(raw_input("Please give me a number to check: "))
check = int(raw_input("Please give me a number to divide by: "))

if num % check == 0:
    print "%d divides evenly into %d" % (check, num)
else:
    print "%d leaves a remainder when divided by %d" % (num, check)
