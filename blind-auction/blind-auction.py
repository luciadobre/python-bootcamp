import art
import os


print(art.logo)

auction_bids = {}
more_bidders = 'yes'
highest_bid = 0

def add_bids(name, bid):
    auction_bids[name] = bid

while more_bidders == 'yes':
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    add_bids(name, bid)
    more_bidders = input("More bidders?\n")
else:
    print(auction_bids)

for bid in auction_bids:
    if auction_bids[bid] > highest_bid:
        highest_bid = auction_bids[bid]

print(f"The winner is: {list(auction_bids.keys())[list(auction_bids.values()).index(highest_bid)]} with a bid of {highest_bid}")


