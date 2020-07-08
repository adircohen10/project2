from Score import *
from random import randrange
import os
import random
from random import  randint
from Utils import *


lo = 1
hi = 101

# Generate a sequence of random numbers between 1 and 101
def generage_sequence(difficulty):
    print("  ")
    print("Now you are about to see a sequence of " + str(difficulty) + " numbers. After seeing the numbers, enter the numbers you saw, each one separated by Enter.")
    input("press Enter to continue")
    gamelist = [lo + int(random.random() * (hi - lo)) for i in range(difficulty)]
    print(gamelist)
    time.sleep(.700)
    clear_screen()
    return gamelist


# Get a sequence of numbers from user
def get_userlist(difficulty):
    userlist = []
    for i in range(difficulty):
        elements = int(input("Enter your answer"))
        userlist.append((elements))
    return userlist

# Compare between the sequences of the first function and the second function
def is_list_equal(gamelist, userlist):
        if userlist == gamelist:
                return True
        else:
                return False


# Play the game and return result
def MemoryGame(difficulty):
        gamelist = generage_sequence(difficulty)
        userlist = get_userlist(difficulty)
        if is_list_equal(gamelist, userlist):
                add_scores(difficulty)
                return 1


        else:
                print("You Lose")
                return 0

