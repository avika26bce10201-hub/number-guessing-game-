"""
utilities.py
------------
This module provides reusable helper functions for formatted console output,
decorative dividers, and basic input validation.
"""

# Immutable option sets using frozen sets (demonstrating frozenset data structure)
MAIN_MENU_OPTIONS = frozenset(["1", "2", "3"])
DIFFICULTY_OPTIONS = frozenset(["1", "2", "3"])
CONFIRMATION_OPTIONS = frozenset(["y", "Y", "n", "N"])


def print_divider(char="=", length=50):
    """
    Prints a decorative divider line across the console.
    Demonstrates string repetition using arithmetic operator (*).
    """
    print(char * length)


def print_header(title):
    """
    Prints a visually clean section header with surrounding dividers.
    """
    print_divider("=")
    print(f"  {title.upper()}")
    print_divider("=")


def get_menu_choice(prompt, valid_options):
    """
    Prompts the user for input and ensures the choice belongs to valid_options.
    Demonstrates while loop, logical operators, and membership operator (in / not in).

    Parameters:
        prompt (str): The text displayed to the user.
        valid_options (tuple, list, or frozenset): Collection of accepted string inputs.

    Returns:
        str: A validated user input.
    """
    while True:
        user_choice = input(prompt).strip()
        # Using membership operator to validate input
        if user_choice in valid_options:
            return user_choice
        else:
            options_str = ", ".join(sorted(list(valid_options)))
            print(f"Invalid input! Please choose from: {options_str}")

