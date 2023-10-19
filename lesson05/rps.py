# rps rock-paper-scissors GAME 

# Import necessary modules
import sys
import random
from enum import Enum

# Define an Enum for Rock, Paper, Scissors
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Get player's choice as input
playerchoice = input("Enter:\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
# Convert the player's choice to an integer
player = int(playerchoice)

# Check if the player's choice is valid (1, 2, or 3)
if player < 1 or player > 3:
    # If not valid, exit the program with an error message
    sys.exit("You must enter 1, 2, or 3.")

# Randomly generate the computer's choice
computerchoice = random.choice("123")
computer = int(computerchoice)

# Print the player's and computer's choices
print(" ")
print("You Chose " + RPS(player).name + ".")
print("Python Chose " + RPS(computer).name + ".")
print(" ")

# Determine the winner of the game and display the result
if player == 1 and computer == 3:
    print("🎉You Win!!!")
elif player == 2 and computer == 1:
    print("🎉You win!!")
elif player == 3 and computer == 2:
    print("🎉You Win!")
elif player == computer:
    print("😲Tie Game")
else:
    print("🐍Python Wins!")
