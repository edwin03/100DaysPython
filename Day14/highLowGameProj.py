from art import logo, vs
from game_data import data
import random, os

def compare(data, answer):
    if data[0]["follower_count"] > data[1]["follower_count"]:
        return answer == 'a'
    else:
        return answer == 'b'

def getData(num):
    return random.sample(data, num)

def clear():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Linux/Mac
    else:
        _ = os.system('clear')
    
def high_low_game(g_data):
    score = 0
    stillGame = True
    while stillGame == True:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {g_data[0]["name"]}, a {g_data[0]["description"]}, from {g_data[0]["country"]}. {g_data[0]["follower_count"]}")
        print(vs)
        print(f"Against B: {g_data[1]["name"]}, a {g_data[1]["description"]}, from {g_data[1]["country"]}. {g_data[1]["follower_count"]}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        stillGame = compare(g_data, choice)
        clear()
        if stillGame == True:
            score += 1
            g_data[0] = g_data[1]
            g_data[1] = getData(1)[0]
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

g_data = getData(2)
high_low_game(g_data)