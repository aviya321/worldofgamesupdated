from random import randrange
from Score import add_score


def generate_number(number):
    return randrange(int(number))


def get_guess_from_user():
    return int(input('Please guess a number:'))


def compare_results(random_number, user_guess, difficulty):
    if random_number == user_guess:
        print("You are right!")
        add_score(difficulty)
    else:
        print("You are wrong!")
    return random_number == user_guess


def play1(difficulty):
    random_number = generate_number(difficulty)
    user_guess = get_guess_from_user()
    return compare_results(random_number, user_guess, difficulty)












