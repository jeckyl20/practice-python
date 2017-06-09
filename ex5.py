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
from random import *
rand1 = []
rand2 = []

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []
rcommon = []

for i in range(1,25):
    rand1.append(randint(1, 50))
#    print rand1

for i in range(1,20):
    rand2.append(randint(1, 50))
#    print rand2

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

# do the comparison using the longer list?
if len(rand1) > len(rand2):
    for i in rand1:
        if i in rand2 and i not in rcommon:
            rcommon.append(i)
else:
    for i in rand2:
        if i in rand1 and i not in rcommon:
            rcommon.append(i)
print rand1
print rand2
print rcommon

