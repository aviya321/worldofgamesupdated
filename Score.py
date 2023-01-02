from Utils import *
from os import path

def calculate_score(difficulty):
    POINTS_OF_WINNING = int((difficulty*3)+5)
    scores_file = open(SCORES_FILE_NAME, "r")
    current_score = int(scores_file.readline())
    scores_file.close()
    new_score = current_score + POINTS_OF_WINNING
    print(new_score)


def add_score(difficulty):
    if path.exists(SCORES_FILE_NAME):
        new_score = calculate_score(difficulty)
        scores_file = open(SCORES_FILE_NAME, "w")
        scores_file.write(str(new_score))
    else:
        score_file = open(SCORES_FILE_NAME, "w")
        score_file.write("0")
        score_file.close()





