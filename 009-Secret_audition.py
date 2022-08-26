import os
from secret_audition_art import logo

bids = {}
should_continue = True


def find_biggest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(logo)
print("We are about to star the secret audition!")

while should_continue:

    participant = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[participant] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if others == "no":
        should_continue = False
        find_biggest_bid(bids)
    elif others == "yes":
        os.system('cls')
print()
