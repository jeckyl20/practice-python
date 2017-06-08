# vim: set fileencoding=utf_8 :
'''
List Overlap  
Exercise 5 (and Solution)

Take two lists, say for example these two:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

        Extras:

        Randomly generate two lists to test this
        Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []

# do the comparison using the longer list?
if len(a) > len(b):
    for i in a:
        if i in b and i not in common:
            common.append(i)
else:
    for i in b:
        if i in a and i not in common:
            common.append(i)
print common
