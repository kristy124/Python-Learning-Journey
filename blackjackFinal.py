import random
import blackJackArt

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(deck):
    """ deals a card to the deck that's passed as an argument"""
    deck.append(random.choice(cards))


def calc_score(deck):
    """calculates total score of the deck that's passed as an argument"""
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)


def start_game():
    """initiates the game of blackjack"""
    print(blackJackArt.logo)
    player_cards = []
    computer_cards = []

    for i in range(2):
        deal_card(player_cards)
        deal_card(computer_cards)

    continue_playing = True

    while continue_playing:
        player_score = calc_score(player_cards)
        computer_score = calc_score(computer_cards)
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if player_score == 21 or computer_score == 21 or player_score > 21:
            continue_playing = False
        else:
            deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_again == "y":
                deal_card(player_cards)
            else:
                continue_playing = False

    while computer_score < 17:
        deal_card(computer_cards)
        computer_score = calc_score(computer_cards)

    print(f'    Your final hand: {player_cards}, final score: {player_score}')
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    if computer_score == 21 and len(computer_cards) == 2:
        print("Lose, opponent has Blackjack 😱")
    elif player_score == 21 and len(player_cards) == 2:
        print("Win with a Blackjack 😎")
    elif player_score == computer_score:
        print("Draw 🙃")
    elif player_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif computer_score > player_score:
        print("You lose 😤")
    elif player_score > computer_score:
        print("You win 😃")

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        start_game()


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == 'y':
    start_game()