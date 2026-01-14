import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
is_running = True

while is_running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock/ paper/ scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Thats a tie...!")
    elif player == "rock" and computer == "scirrors":
        print("You Won....!")
    elif player == "scissors" and computer == "paper":
        print("You Won....!")
    elif player == "paper" and computer == "rock":
        print("You Won....!")
    else:
        print("You loos...!")

    play_again = input("Want to play again? (Y/N): ").lower()
    if not play_again == "y":
        is_running = False

print("Thanks For Playing...!")