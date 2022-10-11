import random
from os import system, name

from higherLowerArt import logo, vs
from higherLowerGameData import data


def clear():
    """Clears the terminal"""
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def random_account():
    """Returns a random account from data"""
    return random.choice(data)


def print_data_info(account):
    """Takes data info and returns info in a concise sentence"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def play():
    """Starts the game of higher lower"""
    account_a = random_account()
    account_b = random_account()
    while account_a == account_b:
        account_b - random_account()
    current_score = 0
    playing_game = True
    print(logo)
    while playing_game:
        account_a = account_b
        account_b = random_account()
        if account_a == account_b:
            account_b = random_account()
        print(f"Compare A: {print_data_info(account_a)}")
        print(vs)
        print(f"Against B: {print_data_info(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        while guess != 'a' and guess != 'b':
            print("Please enter a valid input.")
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        print(logo)
        if account_a['follower_count'] > account_b['follower_count'] and guess == "a":
            current_score += 1
            print(f"You're right! Current score: {current_score}")
        elif account_b['follower_count'] > account_a['follower_count'] and guess == "b":
            current_score += 1
            print(f"You're right! Current score: {current_score}")
        elif account_a['follower_count'] > account_b['follower_count'] and guess == "b":
            print(f"Sorry, that's wrong. Final score: {current_score}")
            playing_game = False
        elif account_b['follower_count'] > account_a['follower_count'] and guess == "a":
            print(f"Sorry, that's wrong. Final score: {current_score}")
            playing_game = False
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            playing_game = False
    play_again = input("Would you like to play again? Enter 'Y' or 'N'. ").lower()
    while play_again != 'y' and play_again != 'n':
        print("Please enter a valid input.")
        play_again = input("Would you like to play again? Enter 'Y' or 'N'. ").lower()
    if play_again == "y":
        clear()
        play()

play()
