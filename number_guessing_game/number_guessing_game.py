"""Number guessing game implementation."""

from random import randint

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_GUESSES = 10


def read_input() -> float:
    """
    Read user input and return a float.
    
    Rejects invalid input until user enters a valid number.
    
    Returns:
        float: The valid number entered by the user.
    """
    while True:
        try:
            user_input = float(input("\nEnter a number: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")


def main() -> None:
    """
    Main function that runs the game loop.
    
    The game generates a random number between MIN_NUMBER and MAX_NUMBER,
    then prompts the user to guess it, providing feedback on whether
    the guess is too high or too low.
    """
    number_to_guess = randint(MIN_NUMBER, MAX_NUMBER)
    guesses_remaining = MAX_GUESSES
    
    print("Welcome to Guess the Number")
    print(f"I've generated a random number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"Now it's your turn to guess it. You have {MAX_GUESSES} guesses to get it right.")
    
    while guesses_remaining > 0:
        guess = read_input()
        guesses_remaining -= 1

        if guess < number_to_guess:
            print("Your guess is too low.")
            print(f"You have {guesses_remaining} guesses remaining.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
            print(f"You have {guesses_remaining} guesses remaining.")
        else:
            print(f"You guessed it in {MAX_GUESSES - guesses_remaining} guesses!")
            break
    else:
        print(f"\nYou didn't guess it. The number was {number_to_guess}.")
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()