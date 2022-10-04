from auctionArt import logo

print(logo)
print('Welcome to the secret auction program.')

bids = {}
continue_auction = True
while continue_auction:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bids[bidder_name] = bid_amount
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_bidders == 'no':
        continue_auction = False
    # clear the screen

#clear the screen
highest_bid = 0
highest_bidder = ''
for name in bids:
    if bids[name] > highest_bid:
        highest_bid = bids[name]
        highest_bidder = name
print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')
