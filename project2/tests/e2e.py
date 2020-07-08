


#
# 2. main_function() –
# Will call our tests function.
# The main function will return -1 as an OS exit code if the tests failed and 0 if it passed.



# test_scores_service(app_url) – Will test our web service.
# Will get the application URL as an input, open a browser to that URL, select the score
# element in our web page, check that it is a number between 0 to 1000 and return a boolean value if it’s true or not.
from MainScores import *
from MainGameTest import *
from Utils import score_file
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from lxml import html
import requests
driver = webdriver.Firefox(executable_path="/Users/adirc/Downloads/geckodriver")
app_url = driver.get("http://0.0.0.0:8777")
score = driver.find_elements_by_tag_name("div")
url = "http://0.0.0.0:8777"
# page = requests.get(url)
# data = page.text
# soup = BeautifulSoup(data, 'html.parser')
# score = soup.findAll("div", {"id" == "//*[@id="score"]"})
# app_url = driver.get("host='0.0.0.0', debug=True, threaded=True, port=8777")
# score = open(score_file, "r")



def main_function(score):
        while score == True:
                try:
                    if (score >= 0 or score <= 1000):
                        is_user_input_valid = True
                        print('Works')
                        return test_scores_service(score)
                    else:
                        print("Wrong score range")
                        return -1
                except:
                    print("Invalid value. Please enter a number")


def test_scores_service(score):
        # return score
        print(len(score))
        if score == 1 or 2 or 3 or 4 or 5:
            print('yy')
            return 0
        else:
            return -1

    #         user_result = load_game(gamenumber, difficulty)
    #         if user_result == 1:
    #             is_user_won = True
    #
    #
    #
    #
    #
    #
    #
    #
    # app_url = app.run(host='0.0.0.0', debug=True, threaded=True, port=8777)
    # print (app_url)

    # while is_user_won == False:
    #     is_user_input_valid = False
    #     gamenumber = 0
    #     difficulty = 0