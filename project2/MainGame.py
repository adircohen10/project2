from Live import *
from Utils import *

#call Welcome function, call load game function while user is loosing.
welcome(name=input("Please Type Your Name:"))
is_user_won = False
while is_user_won == False:
    is_user_input_valid = False
    gamenumber = 0
    difficulty = 0
    while is_user_input_valid == False:
        try:
            gamenumber = int(input("Please choose a game to play:"))
            difficulty = int(input("Please choose difficulty level from 1-5"))
            if (gamenumber == 1 or gamenumber == 2) and (difficulty >= 1 and difficulty <= 5):
                    is_user_input_valid = True
            else: print("Wrong number range")
        except:
            print("Invalid value. Please enter a number")
    user_result = load_game(gamenumber, difficulty)
    if user_result == 1:
        is_user_won = True