from MemoryGame import  *
from GuessGame import  *
from Utils import *


# Get the user's name
def welcome(name):
        print("Hello  " + name + "  Welcome to the World of Games (WoG).")
        print("Here you can find many cool games to play.")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        print("2. Guess Game - guess a number and see if you choose  as the same as the computer")
        print("   ")


# Get the user's selections
def load_game(gamenumber, difficulty):
    if gamenumber == 1:
            if difficulty in range(1, 6):
                print("You choose to play the Memory Game")
                print("Difficulty level chosen is : " + str(difficulty))
                print("  ")
                return MemoryGame(difficulty)
            else:
                return error_message()
    elif gamenumber == 2:
                if difficulty in range(1, 6):
                    print("You choose to play the Memory Game")
                    print("Difficulty level chosen is : " + str(difficulty))
                    print("  ")
                    return generate_number(difficulty)

                else:
                    return error_message()
    else:
                return error_message()










