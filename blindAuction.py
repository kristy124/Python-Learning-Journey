from auctionArt import logo

print(logo)
print('Welcome to the secret auction program.')

# Udemy Solution
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     highest_bidder = ''
#     for name in bidding_record:
#         if bidding_record[name] > highest_bid:
#             highest_bid = bidding_record[name]
#             highest_bidder = name
#     print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')

bids = {}
continue_auction = True
while continue_auction:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bids[bidder_name] = bid_amount
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_bidders == 'no':
        continue_auction = False
        find_highest_bidder(bids)
    # clear the screen

#clear the screen
highest_bid = 0
highest_bidder = ''
for name in bids:
    if bids[name] > highest_bid:
        highest_bid = bids[name]
        highest_bidder = name
print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')