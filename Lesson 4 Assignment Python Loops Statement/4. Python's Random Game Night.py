# Objective:
# The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.

# Task 1: Random Choice Game
# Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.

import random
sports = ["Baseball", "Basketball", "Football", "Soccer", "Tennis", "Golf", "Hockey", "Volleyball"]
randomly_chosen = random.choice(sports)
player_chosen = input("Select a sport: Baseball, Basketball, Football, Soccer, Tennis, Golf, Hockey, Volleyball")

if randomly_chosen.lower() == player_chosen.lower():
    print("You chose the same as the computer")
else:
    print(f"You chose {player_chosen} but the computer randomly chose {randomly_chosen}")