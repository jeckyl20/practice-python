# vim: set fileencoding=utf_8 :
'''
Password Generator    
Exercise 16 (and Solution)

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''
import string
import random

def genPassword():
    print "Let me generate a strong random password for you."
    password = ""
#    lletters = list(string.ascii_lowercase)
#    uletters = list(string.ascii_uppercase)
#    numbers = range(0,10)
#    symbol = list(string.punctuation)
#    randchar = lletters + uletters + numbers + symbol
    randchar = list(string.ascii_lowercase) + list(string.ascii_uppercase) + range(0,10) + list(string.punctuation)
    rlength = random.randint(10, 24)
    while len(password) < rlength:
        password += str(random.choice(randchar))
    return password

if __name__ == "__main__":
    wlist = ["Write","a","password","generator","in","Python.","Be","creative","with","how","you","generate","passwords","-","strong","password","s","have","a","mix","of","lowercase","letters,","uppercase","letters,","numbers,","and","symbols.","The","passwords","should","be","random,","generating","a","new","password","every","time","the","user","asks","for","a","new","password.","Include","your","run-ti","me","code","in","a","main","method"]
    passtype = raw_input("Do you want a strong or a weak password? ").lower()
    if passtype == "strong":
        print genPassword()
    elif passtype == "weak":
        weakpass = random.sample(wlist, 2)
        print ''.join(weakpass)
    else:
        print "I guess you don't know what you want."
