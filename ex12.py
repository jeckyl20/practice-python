# vim: set fileencoding=utf_8 :
'''
List Ends 
Exercise 12 (and Solution)

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''

a = [5, 10, 15, 20, 25]
b = [1, 2, 3, 4, 5]

def get_elements(x):
    fl = []
    fl.append(x[0])
    fl.append(x[-1])
    return fl

if __name__ == "__main__":
    print get_elements(a)
    print [ i for i in b if i == b[0] or i == b[-1]]
