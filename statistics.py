"""
statistics.py
-------------
This module handles score calculations and formatting and displaying
statistics for the Number Guessing Game.
"""

from utilities import print_header, print_divider


def calculate_score(won, attempts_used, max_attempts):
    """
    Calculates the score for a game round.
    
    Formula:
        If won: score = maximum_score - (attempts_used - 1) * 10
        If lost: score = 0
    
    Parameters:
        won (bool): Whether the player successfully guessed the number.
        attempts_used (int): Number of guesses made in this round.
        max_attempts (int): Maximum attempts allowed for the difficulty.

    Returns:
        int: The computed score for the round.
    """
    if not won:
        return 0

    maximum_score = 100
    # Formula demonstration with arithmetic operators
    deduction = (attempts_used - 1) * 10
    score = maximum_score - deduction

    # Ensure a minimum score of 10 for any correct guess
    if score < 10:
        score = 10

    return score


def display_player_stats(player):
    """
    Displays the cumulative statistics of the given player in a structured format.

    Parameters:
        player (Player): An instance of the Player class.
    """
    print_header(f"Performance Statistics for {player.name}")
    print(f" Total Games Played  : {player.games_played}")
    print(f" Games Won           : {player.games_won}")
    print(f" Games Lost          : {player.games_lost}")
    print(f" Win Percentage      : {player.get_win_percentage()}%")
    print(f" Total Attempts Made : {player.total_attempts}")
    print(f" Average Attempts    : {player.get_average_attempts()}")
    print(f" Total Accumulated Score: {player.total_score}")
    print_divider("-")
