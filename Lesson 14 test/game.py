import random

def play_game():
    secret_number = random.randint(1, 50)
    hearts = 5

    print("Welcome to the number guessing game")
    print("guess the number I am thinking of between 1 and 50. \nYou have 5 attempts")

    while hearts > 0:
        print(f"Hearts left: {hearts}")

        user_input = input("Enter your guess: ")
        if not user_input.isdigit():
            print("INVALID NUMBER")
            continue
        guess = int(user_input)

        difference = abs(secret_number - guess)

        if guess == secret_number:
            print("You guessed the correct number!!!")
        elif difference <= 5:
            print("HOT!!! you are very close to the number")
        elif difference <= 15:
            print("WARM! you are getting closer to the number")
        elif difference <= 30:
            print("COLD! you are a little bit far from the number")
        else:
            print("ICE COLD!!! you are very far from the number")

        if guess < secret_number:
            print("Hint : guess higher")
        else:
            print("Hint : guess lower")

        hearts -= 1
        print("You lost a heart! \n")
    if hearts == 0:
        print("===GAME OVER===")

play_game()
