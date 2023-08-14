import yaml
import random

with open("game_reqirements.yaml","r") as f:
    config = yaml.safe_load(f)

range_min = config['range']['min']
range_max = config['range']['max']
guesses = config['guesses']

solved = False

for i in range(guesses):

    correct_no = random.randint(range_min, range_max)
    player_guess = int(input("Enter your guess: "))
    if player_guess == correct_no:
        print(f"Correct! You did it in {i + 1} guesses.")
    elif player_guess < correct_no:
        print("Too low")
    elif player_guess > correct_no:
        print("Too high")