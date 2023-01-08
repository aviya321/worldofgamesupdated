from GuessGame import play1
from MemoryGame import play2
from CurrencyRouletteGame import play3

# The function has a person name and returns a string
def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play:")


# The function prints out the following text and make sure numbers are between 1-3, 1-5
def load_game():
    while True:
        game_chosen = input('''
        Please choose a game to play:
        1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
        2.Guess Game - guess a number and see if you chose like the computer.
        3.Currency Roulette - try and guess the value of a random amount of USD in ILS.
        ''')

        while not 3 >= int(game_chosen) >= 1:
            game_chosen = input('its not a valid number, please try again')
            while not game_chosen.isdigit():
                game_chosen = input('its not a valid number, please try again')
        print('Thank you, you have entered game number:', game_chosen)

        break

    while True:
        difficulty = (input('Please choose a level of difficulty to select from 1 to 5:'))
        while not 5 >= int(difficulty) >= 1:
            difficulty = input('its not a valid number, please try again')
            while not difficulty.isdigit():
                difficulty = input('its not a valid number, please try again')
        print('Thank you, you have entered level of difficulty:', difficulty)

        break

    if game_chosen == 1:
        GuessGame.play1(difficulty)
    if game_chosen == 2:
        MemoryGame.play2(difficulty)
    if game_chosen == 3:
        CurrencyRouletteGame.play3(difficulty)









