from art import logo
import os

# TODO-4: Compare bids in dictionary
def find_highest(bidders):
	hBid = 0
	for name in bidders:
		if bidders[name] > hBid:
			hName = name
			hBid = bidders[name]

	print(f"This winner is {hName} with a bid of ${bidders[hName]}")

print(logo)
bids = {}
cont = True

while cont:
	# TODO-1: Ask the user for input
	name = input(f"What is your name?: ")
	# TODO-2: Save data into dictionary {name: price}
	bid = int(input(f"What is your bid?: "))
	bids[name] = bid
	# TODO-3: Whether if new bids need to be added
	cont = input("Are there any other bidders? Type 'yes or no'.\n").lower()
	if cont == 'no':
		cont = False
		find_highest(bids)
	else:
		if os.name == 'nt':  # for windows
			os.system('cls')
		else:  # for unix/linux/mac
			os.system('clear')