from Utils import *
from MainScores import *


# Add the user score to Scores.txt
def add_scores(points):
    file = open(score_file, "w+")
    file.write(str(points))
    file.close()
    print("You Won")
    score_server()
    print("Launching http://0.0.0.0:8777/ to see the score")