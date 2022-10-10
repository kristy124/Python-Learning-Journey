import random

import higherLowerArt
from higherLowerGameData import data

def random_account():
    """Selects a random account from data"""
    return random.choice(data)


def print_data_info(account):
    """Returns data info in a concise sentence"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def play():
    """Starts the game of higher lower"""
    account_a = random_account()
    account_b = random_account()
    current_score = 0
    playing_game = True
    print(higherLowerArt.logo)
    while playing_game:
        account_a = account_b
        account_b = random_account()
        print(f"Compare A: {print_data_info(account_a)}")
        print(higherLowerArt.vs)
        print(f"Against B: {print_data_info(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        # clear screen
        print(higherLowerArt.logo)
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


play()
