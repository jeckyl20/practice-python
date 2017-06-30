# vim: set fileencoding=utf_8 :
'''
Fibonacci  
Exercise 13 (and Solution)

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def gen_fib(x):
## Recursive way from python book
#    if x == 0 or x == 1:
#        return 1
#    else:
#        return gen_fib(x-1) + gen_fib(x-2)
## Using a list and compute elements
    flist = []
    if x == 0:
        return flist
    elif x == 1:
        flist.append(1)
        return flist
    else:
        for i in range(0,x+1):
            if len(flist) == 0:
                flist.append(1)
#                print "Index = %d" % i
#                print flist
            elif len(flist) == 1:
                flist.append(1)
#                print "Index = %d" % i
#                print flist
            else:
#                print "Index = %d" % i
#                print "Else clause: %s" % flist
#                print "Index %d - 1 = %d" % (i, flist[i-1])
#                print "Index %d - 2 = %d" % (i, flist[i-2])
                flist.append(flist[i-1] + flist[i-2])
        return flist

if __name__ == "__main__":
    try:
        num = int(raw_input("How many Fibonnaci numbers would you like go generate?: "))
        print gen_fib(num)
## How to call recursive version
#        for i in range(num+1):
#            print gen_fib(i)
    except ValueError:
        print "That's not an int!"
