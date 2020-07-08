from flask import Flask
from Utils import *


app = Flask(__name__)

# Get the score of the user and return it to HTML file
@app.route('/')
def score_server():
    try:
        score = open(score_file, "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
            <link rel="icon" href="data:,">
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + error_message() + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
            <link rel="icon" href="data:,">
        </head>
        <body>
            <h1>The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True, threaded=True, port=8777)
