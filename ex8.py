# vim: set fileencoding=utf_8 :
'''
Rock Paper Scissors   
Exercise 8 (and Solution)

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''
plays = ["rock", "paper", "scissors"]

def rules(val1, val2):
    if val1 == val2:
        return "Tie"
    elif val1 == "rock" and val2 == "scissors":
        return "P1 wins"
    elif val1 == "rock" and val2 == "paper":
        return "P2 wins"
    elif val1 == "scissors" and val2 == "paper":
        return "P1 wins"
    elif val1 == "scissors" and val2 == "rock":
        return "P2 wins"
    elif val1 == "paper" and val2 == "rock":
        return "P1 wins"
    else:
        return "P2 wins"

while quit != "no":
## Get player1 input
    p1 = raw_input("PLAYER1 - Please choose rock, paper, or scissors: ")
    while p1.lower() != "rock" or p1.lower() != "paper" or p1.lower() != "scissors":
#        print "You chose: %s" % p1
        if p1.lower() in plays:
            break
## if the input is bad keep prompting for a valid play
        else:
            p1 = raw_input("PLAYER1 - Please choose rock, paper, or scissors: ")
## Get player2 input
    p2 = raw_input("PLAYER2 - Please choose rock, paper, or scissors: ")
    while p2.lower() != "rock" or p2.lower() != "paper" or p2.lower() != "scissors":
#        print "You chose: %s" % p2
        if p2.lower() in plays:
            break
## if the input is bad keep prompting for a valid play
        else:
            p2 = raw_input("PLAYER2 - Please choose rock, paper, or scissors: ")
    check = rules(p1, p2)
    print check
    quit = raw_input("Would you like to play again? Type 'no' to end the game: ")
    if quit.lower() == "no":
        break
