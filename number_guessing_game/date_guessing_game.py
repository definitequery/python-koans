"""Date guessing game implementation."""

import json
from random import choice
from datetime import date
from typing import List, Dict, Optional

# Constants
MAX_GUESSES = 3


def read_dates() -> List[Dict[str, str]]:
    """
    Read the dates.json file and return a list of events and dates.
    
    Returns:
        List[Dict[str, str]]: List of dictionaries containing event and date data.
    """
    with open("dates.json", "r") as f:
        return json.load(f)


def read_year() -> int:
    """
    Read user input and return a valid year.
    
    Returns:
        int: The valid year entered by the user.
    """
    while True:
        try:
            year = input("\nEnter your guess: ")
            return int(year)
        except ValueError:
            print("Invalid input. Please enter a valid year.")


def get_random_date(dates: List[Dict[str, str]]) -> Optional[Dict[str, str]]:
    """
    Return a random event and the date it happened from the list of dates.
    
    Args:
        dates: List of dictionaries containing event and date data.
        
    Returns:
        Optional[Dict[str, str]]: Random event dictionary or None if list is empty.
    """
    if not dates:
        return None
    return choice(dates)


def main() -> None:
    """
    Main function that runs the game loop.
    
    The game selects a random historical event and prompts the user to guess
    the year it occurred, providing feedback on whether the guess is too early
    or too late.
    """
    dates = read_dates()
    random_date = get_random_date(dates)
    
    if random_date is None:
        print("No events available. Please check the dates.json file.")
        return
    
    date_year = date.fromisoformat(random_date['date']).year

    print("Welcome to the Date Guessing Game!")
    print("I've selected a random event and the year it happened from history.")
    print(f"You have {MAX_GUESSES} guesses to get it right.")
    guesses_remaining = MAX_GUESSES

    while guesses_remaining > 0:
        print(f"\n{random_date['event']}")
        guess = read_year()
        
        if guess < date_year:
            print("That's too early. Try again.")
            guesses_remaining -= 1
            print(f"You have {guesses_remaining} guesses remaining.")
        elif guess > date_year:
            print("That's too late. Try again.")
            guesses_remaining -= 1
            print(f"You have {guesses_remaining} guesses remaining.")
        else:
            print(f"\nYou guessed it! {random_date['event']} happened in {date_year}.")
            break
    else:
        print(f"\nYou didn't guess it. {random_date['event']} happened in {date_year}.")
    
    print("Thanks for playing!")


if __name__ == "__main__":
    main()