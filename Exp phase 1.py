import random

print("================================")
print("   ROCK PAPER SCISSORS GAME")
print("================================")

# Player choices
choices = ["Rock", "Paper", "Scissors"]

# Take player input
player = input("Enter Rock, Paper or Scissors: ")

# Computer randomly selects
computer = random.choice(choices)

print("\nPlayer   :", player)
print("Computer :", computer)

print("\nGame choices successfully generated!")
