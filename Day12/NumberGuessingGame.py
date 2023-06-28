#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

if level == "easy":
    attempts = EASY_LEVEL_TURNS
else:
    attempts = HARD_LEVEL_TURNS


while attempts != 0:
    print(f"You have {attempts} remaining to guess the number.")
    number_guess = int(input("Make a guess: "))

    if number_guess == answer:
        attempts = 0
        print("You Won!")
    elif number_guess > answer:
        attempts -= 1
        print("Too high.")
    elif number_guess < answer:
        attempts -= 1
        print("Too low.")
