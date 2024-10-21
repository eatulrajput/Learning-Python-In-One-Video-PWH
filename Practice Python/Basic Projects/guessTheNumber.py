# Guess the Number: A game where the user has to guess a randomly generated number within a specific range.

import random

def guess_the_number():
    print("Welcome to the Guess The Number game!")

    # Set the range for the random number
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    # Generate a random number within the range
    random_number = random.randint(lower_bound, upper_bound)
    print(f"\n I have selected a number between {lower_bound} and {upper_bound}. Try to get it!")

    # Initialize the guess count
    attempts = 0

    while True:
        # Ask the user for their guess
        try:
            user_guess = int(input("\n Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        #Increment the number of attempts
        attempts+=1

        # Check if the guess is correct
        if user_guess < random_number:
            print("Too low, try again!")
        elif user_guess > random_number:
            print("Too high, try again")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts")
            break

guess_the_number()