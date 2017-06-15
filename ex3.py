'''
List Less Than Ten  
list numbers elements if conditional
Exercise 3 (and Solution)

Take a list, say for example this one:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
      and write a program that prints out all the elements of the list that are less than 5.

      Extras:

      Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
      Write this in one line of Python.
      Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

## first solution
#for i in a:
#    if i < 5:
#        print i

## as a new list
#new = []
#for i in a:
#    if i < 5:
#        new.append(i)
#print new

## ask user for number and return list with numbers smaller than the one provided
new = []
test = int(raw_input("Please give me a number: "))

for i in a:
    if i < test:
        new.append(i)
print new

## Try doing it in one line
print "In one line of python below:"
print [ x for x in a if x <= 20 ]
