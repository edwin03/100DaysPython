from art import logo
import random, os

def dealCards(player, loops):
    '''Pass a list and it will add a number of cards based on the loop number.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(loops):
        player.append(random.choice(cards))

def sumCards(user):
    total = sum(user)
    if 11 in user and total == 21:
        # this indicates a blackjack
        return 0
    elif 11 in user and total > 21:
        # this indicates a blackjack
        user.remove(11)
        user.append(1)
        return sum(user)
    else:
        return total
def clear_screeen():
    # Method 1: Using os.name
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

def playGame():
    clear_screeen()
    print(logo)
    user = []
    comp = []
    dealCards(user,2)
    dealCards(comp,2)
    draw = 'y'

    while draw == 'y':
        print(f"    Your cards: {user}, current score: {sumCards(user)}")
        print(f"    Computer's first card: {comp[0]}")

        if sumCards(user) == 0 or sumCards(comp) == 0 or sumCards(user) > 21:
            draw = 'n'
        else:
            # print(comp)
            draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw == 'y':
                dealCards(user, 1)
        
    while sumCards(comp) < 17 and sumCards(comp) != 0:
        dealCards(comp, 1)

    print(f"Your final haand: {user}, final score: {sumCards(user)}")
    print(f"Computer's final hand: {comp}, final score: {sumCards(comp)}")

    if sumCards(user) == 0:
        print("You win with a Blackjack!")
    elif sumCards(comp) == 0:
        print("You lose, computer has a Blackjack!")
    elif sumCards(user) > 21:
        print("You lose!")
    elif sumCards(comp) > 21:
        print("You win!")
    elif sumCards(user) > sumCards(comp):
        print("You win!")
    elif sumCards(user) < sumCards(comp):
        print("You lose!")
    else:
        print("It's a draw!")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    playGame()