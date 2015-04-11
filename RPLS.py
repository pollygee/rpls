# Rock-paper-scissors-lizard-Spock Program

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
# convert number to a name 
def number_to_name(number):
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        return "Number not valid"
    
   
# convert name to number 
    
def name_to_number(name):
    if(name == "rock"):
        return 0
    elif(name == "Spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif(name == "lizard"):
        return 3
    elif(name == "scissors"):
        return 4
    else:
        return "Error"
    
    


def rpsls(name): 
    print "Player Chooses " + name
    player_number = name_to_number(name)
    computer_number = random.randrange(0, 4)
    print "Computer Chooses " + number_to_name(computer_number)
    difference = (player_number - computer_number) % 5
    if ((difference == 3) or (difference ==4)):
        print "Computer Wins!"
    elif ((difference == 1) or (difference ==2)):
        print "Player Wins!"
    elif (difference == 0):
        print "Player and Computer tie!"
    else:
        print "Something is wrong"
    print "\n"
        

 
print "Rock Paper Scissors Lizard Spock Game!"
print "\n"
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")