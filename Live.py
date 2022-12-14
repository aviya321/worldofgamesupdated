# The function has a person name and returns a string
def welcome_name():
    name = input("Please enter your name: ")
    print("Hello" + " " + name + " " + "and welcome to the World of Games (WoG).\nHere you can find many cool games to play:")

welcome_name()

# The function prints out the following text and make sure numbers are between 1-3, 1-5
def load_game():
    print("1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n2.Guess Game - guess a number and see if you chose like the computer\n3.Currency Roulette - try and guess the value of a random amount of USD in ILS")

    game_chosen = (input('Please choose a game to select from 1 to 3:'))

    while not 3 >= int(game_chosen) >= 1:
        game_chosen = input('its not a valid number, please try again')
        while not game_chosen.isdigit():
            game_chosen = input('its not a valid number, please try again')
    print('Thank you, you have entered game number:',game_chosen)

    difficulty_chosen = (input('Please choose a level of difficulty to select from 1 to 5:'))
    while not 5 >= int(difficulty_chosen) >= 1:
        difficulty_chosen = input('its not a valid number, please try again')
        while not difficulty_chosen.isdigit():
            difficulty_chosen = input('its not a valid number, please try again')
    print('Thank you, you have entered level of difficulty:',difficulty_chosen)

load_game()

