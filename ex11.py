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

def is_prime(x):
    if num == 1:
        return "One is not a prime number."
    else:
        for i in range(2,num):
            if num % i == 0:
                return "Cond2: %d is not a prime number. It is divisible by %d" % (num, i)
        return "Cond3: %d is a prime number." % num


if __name__ == "__main__":
    num = int(raw_input("Please give me a number to test: "))
    print is_prime(num)
