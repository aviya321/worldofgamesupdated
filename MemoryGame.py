from random import random, randint
import os
from time import sleep


def generate_sequence(difficulty):
    random_list = []
    for numbers in range(difficulty):
        random_list.append(randint(1, 101))
    print(random_list)
    sleep(0.7)
    os.system('cls')
    return random_list


def get_list_from_user(difficulty):
    user_list = []
    for numbers in range(difficulty):
        user_list.append(int(input('Please enter the numbers you have just seen:')))
    return user_list


def is_list_equal(random_list, user_list):
    if random_list == user_list:
        print('results are equal - you win!')
    else:
        print('results are not equal - you lose!')

    return random_list == user_list


def play2(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    return is_list_equal(random_list, user_list)




