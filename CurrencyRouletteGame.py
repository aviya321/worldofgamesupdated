

import random
from currency_converter import CurrencyConverter

from Score import add_score


def get_money_interval(difficulty):
    c = CurrencyConverter()
    crncy = c.convert(1, 'USD', 'ILS')
    f_crncy = float(crncy)
    secret_number = random.randint(1, 100)
    print("Your random number is", secret_number, "dollars")
    print(f"What do you think will be the {secret_number} in ILS? ")
    suggested_guess = get_guess_from_user()
    real_number = secret_number * f_crncy
    if (real_number - (5 - difficulty)) < suggested_guess < (real_number + (5 - difficulty)):
        print("You are very close! You win!")
        add_score(difficulty)

        return True
    else:
        print("You are very far! You lose!")
        add_score(difficulty)

        return False





def get_guess_from_user():
    user_guess = int(input("Please guess the value of the amount:"))
    return user_guess



def play3(difficulty):
    get_money_interval(difficulty)
