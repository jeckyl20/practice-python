# vim: set fileencoding=utf_8 :
'''
Reverse Word Order   
strings
Exercise 15 (and Solution)

Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''

str1 = raw_input("Please give me a long string containing multiple words: ").split(" ")

def reverse_print(a):
    for i in reversed(a):
        print i, 

if __name__ == "__main__":
    reverse_print(str1)
