# TODO: Add the imports for the logo and random functions.
from art import logo, vs
from game_data import data
import random
# TODO: Create a function that accecpts game_data and display the data, and does the comparison.
def high_low_game(data):
    print(logo)
    keys = random.sample(data, 1)
    print(f"Here {keys[0]}")

high_low_game(data)