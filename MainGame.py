from Live import load_game, welcome

name = input('What is your name?')
welcome(name)
load_game()


def play_again():
    again = input("Do you want to try again? Y/N?")
    if again == "Y" or again == "y":
        return play()
    else:
        print("Thanks for your time. Hope you enjoyed!")






