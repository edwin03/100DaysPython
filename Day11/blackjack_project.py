from art import logo
import random, os

def dealCards(player, loops):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(loops):
        player.append(random.choice(cards))

def sumCards(user, ace):
    total = 0
    for card in user:
        total += card
    if ace == True:
        return total - 11
    else:
        return total

user = []
comp = []

print(logo)

dealCards(user,2)
dealCards(comp,2)

print(f"Your cards: {user}, current score: {sumCards(user)}")
print(f"Computer's first card: {comp[0]}")

if sumCards(user) == 21:
    print("You win!")
elif sumCards(comp) == 21:
    print("You lose!")
elif sumCards(user) > 21:
    if "11" in user:
        if sumCards(user, True) > 21:
            print("You lose!")
else:
    draw = input("Type 'y' to get another card, type 'n' to pass: ")

if draw == True:
    dealCards(user, 1)
elif sumCards(comp) < 17:
    dealCards(comp, 1)

print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

