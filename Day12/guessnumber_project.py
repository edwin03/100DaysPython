from art import logo
import random

def randomNum():
    return random.randint(1, 100)

def playGame(level, num):
    if level == "easy":
        attempts = 10
    else:
        attempts = 5
    for _ in range(attempts+1):
        if _ < attempts:
            print(f"You have {attempts - _} remainaing to geuess the number.")
            guess = int(input("Make a guess: "))
        if _ == attempts:
            print(f"You lose! The number was {num}")
        elif guess == num:
            print(f"You got it! The answer was {num}")
            break
        elif guess > num:
            print("Too high.")
        else:
            print("Too low.")

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()

playGame(level, randomNum())