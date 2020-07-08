



from MainScores import *
from bs4 import BeautifulSoup
from selenium import webdriver

import requests
url = "http://0.0.0.0:8777"

def test_scores_service(url):
    driver = webdriver.Firefox(executable_path="/Users/adirc/Downloads/geckodriver")
    driver.get(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if (len(soup) >= 0 or len(soup) <= 1000):
            return True
    else:
                return False


if __name__ == '__main__':
    def main_function():
        score = test_scores_service(url)
        if score == True:
            return 0
        else:
            return -1
test_scores_service(url)





