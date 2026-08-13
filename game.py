import random

print("===================================")
print("     ROCK, PAPER, SCISSORS GAME")
print("===================================")

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while True:

    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    player = input("Enter your choice: ").lower()

    if player == "4" or player == "exit":
        break

    if player == "1":
        player = "rock"
    elif player == "2":
        player = "paper"
    elif player == "3":
        player = "scissors"
    else:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(choices)

    print("\nYou chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("Result: It's a Draw!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):

        print("Result: You Win! 🎉")
        player_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("-------------------------------")
    print("Your Score     :", player_score)
    print("Computer Score :", computer_score)
    print("-------------------------------")

print("\n===================================")
print("             FINAL SCORE")
print("===================================")
print("Your Score     :", player_score)
print("Computer Score :", computer_score)

if player_score > computer_score:
    print("Congratulations! You are the Winner! 🎉")
elif computer_score > player_score:
    print("Computer wins the game!")
else:
    print("The game ended in a Draw!")

print("Thank you for playing!")