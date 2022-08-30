import random
import os
from Blackjack_art import logo

print("Welcome to blackjack")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):

    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_hands(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_card = []
    dealer_card = []
    game = True

    for card in range(2):
        user_card.append(deal_card())
        dealer_card.append(deal_card())

    while game:
        user_score = (calculate_score(cards=user_card))
        computer_score = (calculate_score(cards=dealer_card))
        print(f"Your hand is {user_card} with a score of {user_score}")
        print(f"The computer has an {dealer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game = False
        else:
            user_should_deal = input("Type 'y' to get another card, or 'n' to pass: ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                game = False
        while computer_score != 0 and computer_score < 17:
            dealer_card.append(deal_card())
            computer_score = calculate_score(dealer_card)

        print(compare_hands(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls")
    play_game()
