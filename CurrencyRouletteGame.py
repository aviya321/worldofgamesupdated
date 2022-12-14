
import random
from currency_converter import CurrencyConverter
print("Hello and welcome to Currency Roulette Game!")


def get_secret_num():
    global secret_number
    secret_number = random.randint(1, 100)
    print("Your random number is", secret_number, "dollars")


def get_guess_from_user():
    difficulty = input("Please enter again your level of difficulty:")
    while not difficulty.isdigit():
        difficulty = int(input('its not a valid number, please try again'))
    print('Thank you, you have entered difficulty:', difficulty)
    c = CurrencyConverter()
    crncy = c.convert(1, 'USD', 'ILS')
    user_guess = int(input("Please enter your suggested value of dollars above in ILS: "))
    guess = round(user_guess / crncy)
    print(f"Your exchange rate is {guess} dollars")
    global diff_sec_guess
    diff_sec_guess = int(secret_number - guess)
    global abs_diff_sec_guess
    abs_diff_sec_guess = abs(diff_sec_guess)
    print(f"You are {abs_diff_sec_guess} shekels far from the real number")
    if int(abs_diff_sec_guess) < int(difficulty):
        print("You are very close! You win!")
    else:
        print("You are very far! You lose!")

def play_again():
    global again
    again = input("Do you want to try again? Y/N?")
    if again == "Y" or again == "y":
        return play()

    else:
        print("Thanks for your time. Hope you enjoyed!")


def play3():
    get_secret_num()
    get_guess_from_user()
    play_again()

play3()

