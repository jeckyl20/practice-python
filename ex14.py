# vim: set fileencoding=utf_8 :
'''
Exercise 14 (and Solution)

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
import random

## Define our lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [1, 2, 1, 5, 1, 7, 10]

rand1 = [ random.randint(1,20) for y in range(1,15) ]
rand2 = [ random.randint(1,50) for y in range(1,21) ]

## Function to find common elements in list
def get_uniq(a):
    unique = []
#    unique = [ i for i in a if i not in unique ]
    for i in a:
        if i not in unique:
            unique.append(i)
    print "List a: %s" % a
    print unique

def get_uniq_set1(a):
    return list(set(a))

def get_uniq_set(a, b):
    '''Use sets to get the union of two lists'''
    return set(a).union(set(b))

if __name__ == "__main__":
    get_uniq(c)
    print get_uniq_set1(c)
    print get_uniq_set(a,b)
    print get_uniq_set(rand1,rand2)
