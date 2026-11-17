# Rock Paper Scissors

import random

while True:
    user_action = input("Enter a choice (roc, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    # using random functions
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}. \n")

    # Conditions to check who won
    if user_action == computer_action:
        print(f"Both players selected {user_action}, Its a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissor! You Win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
           print("Paper covers rock! You Win!")
        else:
            print("Scissors cut paper! You lose!")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("Scissor cuts paper! You Win!")
        else:
            print("Rock smashes scissors! You lose!")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
