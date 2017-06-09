# vim: set fileencoding=utf_8 :
'''
List Comprehensions  
Exercise 7 (and Solution)

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## I first tried i % 2 == 0 for i in a, but that just returns True or False if it is even
even = [i for i in a if i % 2 == 0]
print even
