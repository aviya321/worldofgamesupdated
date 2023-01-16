from random import randint
import os
from time import sleep

from Score import add_score


def generate_sequence(difficulty):
    random_list = []
    for numbers in range(difficulty):
        random_list.append(randint(1, 101))
    print(type(random_list[0]))
    sleep(0.7)
    os.system('cls')
    return random_list


def get_list_from_user(difficulty):
    user_list = input('Please enter the numbers you have just seen:').split(" ")
    user_list = [int(i) for i in user_list]
    return user_list




def is_list_equal(random_list, user_list,difficulty):
    print(random_list)
    print(user_list)
    if random_list == user_list:
        print('results are equal - you win!')
        add_score(difficulty)
        return True
    else:
        print('results are not equal - you lose!')
        return False


def play2(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    return is_list_equal(random_list, user_list,difficulty)

