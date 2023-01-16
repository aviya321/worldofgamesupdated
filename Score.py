from Utils import *
from os import path


def add_score(difficulty):
    new_score = (difficulty * 3) + 5
    try:
        if not os.path.getsize("Scores.txt") == 0:
            with open("Scores.txt", "r") as score_file:
                current_score = score_file.readline()
                print(current_score)
                new_score += int(current_score)
    except FileNotFoundError:
        with open("Scores.txt", "w") as score_file:
            score_file.write(str(new_score))
            print(new_score)

    else:
        with open("Score.txt", "w") as score_file:
            score_file.write(str(new_score))
            print(new_score)















