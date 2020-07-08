
import random
from Score import *
from Utils import *

# Generate a random number between 1 and the difficulty lever the user chose, and run the game and return result
def generate_number(difficulty):
        for x in range(difficulty):
                secretnum = (random.randint(1,difficulty))
        usernum = int(input("Enter your Guess")) in range(difficulty+1)
        if usernum == secretnum:
                add_scores(difficulty)
                return 1
        else:
                print("You Lose")
                return 0





