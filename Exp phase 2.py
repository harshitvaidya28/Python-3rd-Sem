  import random

print("================================")
print("   ROCK PAPER SCISSORS GAME")
print("================================")

player_score = 0
computer_score = 0

while True:

    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1/2/3): ")

    choices = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors"
    }

    if choice not in choices:
        print("Invalid choice!")
        continue

    player = choices[choice]
    computer = random.choice(
        ["Rock", "Paper", "Scissors"]
    )

    print("\nPlayer   :", player)
    print("Computer :", computer)

    # Game logic
    if player == computer:
        print("Result: Draw!")

    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):

        print("Result: Player Wins!")
        player_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\nPlayer Score   :", player_score)
    print("Computer Score :", computer_score)

    again = input("\nPlay again? (yes/no): ")

    if again.lower() != "yes":
        break
