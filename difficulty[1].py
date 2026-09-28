"""
difficulty.py
-------------
This module manages the difficulty levels for the Number Guessing Game.
It stores settings for Easy, Medium, and Hard modes using dictionaries and tuples.
"""

# Dictionary storing difficulty configurations.
# Key: Menu option ("1", "2", "3")
# Value: Tuple containing (Difficulty Name, Minimum Value, Maximum Value, Maximum Attempts)
DIFFICULTY_CONFIG = {
    "1": ("Easy", 1, 50, 10),
    "2": ("Medium", 1, 100, 7),
    "3": ("Hard", 1, 200, 5)
}


def display_difficulty_menu():
    """
    Displays the difficulty selection options to the player.
    """
    print("\n--- Select Difficulty Level ---")
    print("1. Easy   -> Range: 1 to 50  | Attempts: 10")
    print("2. Medium -> Range: 1 to 100 | Attempts: 7")
    print("3. Hard   -> Range: 1 to 200 | Attempts: 5")


def get_difficulty_settings(choice):
    """
    Retrieves the settings for a given difficulty choice.

    Parameters:
        choice (str): The user's menu choice ("1", "2", or "3").

    Returns:
        dict: A dictionary with 'name', 'range' (as a tuple), and 'max_attempts',
              or None if the choice is invalid.
    """
    # Use membership operator to validate choice
    if choice in DIFFICULTY_CONFIG:
        name, low, high, max_attempts = DIFFICULTY_CONFIG[choice]
        return {
            "name": name,
            "range": (low, high),
            "max_attempts": max_attempts
        }
    return None
