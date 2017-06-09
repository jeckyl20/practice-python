# vim: set fileencoding=utf_8 :
'''
String Lists  
strings lists index
Exercise 6 (and Solution)

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

uword = raw_input("Please give me a word: ")
# lets create a reversed copy of our word
rword = uword[::-1]

# For each element of our list, compare it in the original and the reversed list to see if it is the same
for i in range(len(uword)):
    if uword[i] == rword[i]:
#        print uword[i]
#        print rword[i]
        # if our letter is the same, lets check if its the last element in the list
        if len(uword) - i == 1:
            print "%s is a palindrome." % uword
    # if the letter is not the same then its not a palindrome
    else:
        print "%s is not a palindrome." % uword
        break

