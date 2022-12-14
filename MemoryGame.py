import random
import time
import os
from time import sleep

def generate_sequence():
    global difficulty
    difficulty = int(input("Please enter again your level of difficulty:"))
    random_list = []
    for numbers in range(difficulty):
        random_list.append(random.randint(1, 102))
        sleep(0.7)
        os.system('cls')
    print(random_list)



def get_list_from_user():
    global get_list
    get_list = input("Please enter the numbers you have just seen,seprated by space:")
    global get_list_split
    get_list_split = get_list.split()
    global get_user_input
    get_user_input = list(map(int, get_list_split))
    print(get_user_input)



def is_list_equal():
    if get_user_input == []:
        print('results are equal - you win!')
    else:
        print('results are not equal - you lose!')

def play_again():
    global again
    again = input("Do you want to try again? Y/N?")
    if again == "Y" or again == "y":
        return play()

    else:
        print("Thanks for your time. Hope you enjoyed!")



def play2():
    generate_sequence()
    get_list_from_user()
    is_list_equal()
    (play_again())

play2()