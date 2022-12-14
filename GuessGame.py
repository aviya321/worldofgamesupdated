import random

def get_guess_from_user():
    global difficulty
    difficulty = input("Please enter again your difficulty level:")
    while not difficulty.isdigit():
        difficulty = input("It is not a valid number,please try again!")
    global get_guess
    get_guess = input("Please enter a number between 1 and your difficulty level:")
    while not get_guess.isdigit():
        get_guess = input("It is not a valid number,please try again!")
    print(f"Your guess number is {get_guess}")



def generate_number():
    global secret_number
    secret_number = random.randint(1,int(difficulty))
    print(f"Your secret number is {secret_number}")


def compare_results():
    if secret_number == get_guess:
        print("Your guess is perfect! You win!")
    else:
        print("You guess is wrong! You lose!")

def play_again():
    global again
    again = input("Do you want to try again? Y/N?")
    if again == "Y" or again == "y":
        return play()

    else:
        print("Thanks for your time. Hope you enjoyed!")

def play1():
    get_guess_from_user()
    generate_number()
    compare_results()
    play_again()

play1()





