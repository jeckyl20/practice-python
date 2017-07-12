# vim: set fileencoding=utf_8 :
'''
Check Primality Functions   
Exercise 11 (and Solution)

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
'''
'''
## example from the site to have a default for the variable help_text if nothing is passed
def get_integer(help_text="Give me a number: "):
   return int(input(help_text))

age = get_integer("Tell me your age: ")
school_year = get_integer()
if age > 15:
  print("You are over the age of 15")
print("You are in grade " + str(school_year))
'''
'''
After talking to Joe:
    Joes test number: 2147483647
    Create a file with the list of known prime numbers
    If the new prime we are checking for is above the largest element, maybe the last one, then append
    If not, then just use the list to see if it is divisble by a known prime
    http://www.counton.org/explorer/primes/checking-if-a-number-is-prime/
    http://www.prime-numbers.net/how-do-i-find-prime-numbers.html
'''
import sys

def prime_file(x, y):
    try:
        with open("primes.txt") as pfile:
            primesIntList = []
            for line in pfile:
                print "Line: %s" % line
                primesIntList.append(int(line))
                print "primesIntList - in loop: %s" % primesIntList
## check last line of file to see if it is smaller than the square root of our number to test?
            print primesIntList
            print primesIntList[-1]
            print "Variable for square root is: %d" % y
            if primesIntList[-1] > y:
                print "We should hit this condition."
                for i in primesIntList:
                    if x % i == 0:
                        return "%d is not a prime number. It is divisible by %d" % (x, i)
                        break
                return "Checked prime list. %d is a prime number." % x
## Here we should start generating prime numbers above what we have
#            else:
#                if


#;        if primesIntList[-1] < y:
#;            print "We have a new higher prime number to find."
#;            pfile = open("primes.txt", "a+")
#;            for i in primesIntList:
#;                if x % i == 0:
#;                    return "%d is not a prime number. It is divisible by %d" % (x, i)
#;                    break
#;                elif 
                    
### Use the squareroot as the top number to check against. If i <= sqrtNum
#        for i in primesList:
#            if num % i == 0:
#                return "Cond2: %d is not a prime number. It is divisible by %d" % (num, i)
#        return "Cond3: %d is a prime number." % num
#        else:
#            is_prime(x, y, primesIntList)

## append to the file <filename>.write(<prime> + "\n")
    except IOError as e:
#        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        pfile = open("primes.txt", "a+")
#        pfile.write("Add line from IOError function." + "\n")
#        pfile.close()

def is_prime(num, sqrtNum):
    if num == 1:
        return "One is not a prime number."
    else:
### Use the squareroot as the top number to check against. 
        for i in range(2,sqrtNum+1):
            if num % i == 0:
                return "Cond2: %d is not a prime number. It is divisible by %d" % (num, i)
        return "Cond3: %d is a prime number." % num

if __name__ == "__main__":
    num = int(raw_input("Please give me a number to test: "))
    sqrtNum = int(round(num**(.5)+1))
#    print num
#    print sqrtNum
    print is_prime(num, sqrtNum)
#    print prime_file(num, sqrtNum)
