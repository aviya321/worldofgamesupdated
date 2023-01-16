from MemoryGame import play2
from CurrencyRouletteGame import play3
from GuessGame import play1

# The function has a person name and returns a string
def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play:")


# The function prints out the following text and make sure numbers are between 1-3, 1-5
def load_game():
    not_valid = True
    game_chosen = ""
    while not_valid:
        game_chosen = input(
            "Please choose a game to play:\n1.Guess Game - guess a number and see if you chose like the computer."
            "to guess it back.\n2.Memory Game -a sequence of numbers will appear for 1 second and you have to guess it back.\n3.Currency "
            "Roulette - try and guess the value of a random amount of USD in ILS.\n")

        if not 3 >= int(game_chosen) >= 1:
            game_chosen = input('its not a valid number, please try again')
            continue
        if not game_chosen.isdigit():
            game_chosen = input('its not a valid number, please try again')
            continue
        print('Thank you, you have entered game number:', game_chosen)
        not_valid = False

    checking = True
    while checking:
        difficulty = int(input('Please choose a level of difficulty to select from 1 to 5:'))
        if not 5 >= difficulty >= 1:
            print('its not a valid number, please try again')
            continue
        if not str(difficulty).isdigit:
            print('its not a valid number, please try again')
            continue
        print('Thank you, you have entered level of difficulty:', difficulty)
        pass

        if game_chosen == "1":
            play1(difficulty)
            play_again()
            break
        elif game_chosen == "2":
            play2(difficulty)
            play_again()
            break
        elif game_chosen == "3":
            play3(difficulty)
            play_again()
            break
        else:
            print("Your answer is invalid.Please try again")
            continue

def play_again():
    checking = True
    while checking:
        again = input("Do you want to try again? Y/N?")
        if again == "y" or again == "Y":
            load_game()
        elif again == "n" or again == "N":
            print("Thanks for your time. Hope you enjoyed!")
            checking = False
        else:
            print("You answer is invalid.Please try again")
            continue











