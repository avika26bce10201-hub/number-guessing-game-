"""
player.py
---------
This module defines the Player class to store and update player profile
information and overall performance statistics across game rounds.
"""

import array


class Player:
    """
    A class representing a player in the Number Guessing Game.
    Demonstrates basic Object-Oriented Programming (OOP) concepts.
    """

    def __init__(self, name):
        """
        Initializes a new player profile with the provided name.
        """
        # Instance attributes
        self.name = name
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.total_attempts = 0
        self.total_score = 0
        
        # Array data structure (from Python's standard array module)
        # 'i' specifies a signed integer array to store individual round scores
        self.score_history = array.array('i', [])

    def record_game(self, won, attempts, score):
        """
        Updates the player's cumulative statistics after completing a game round.

        Parameters:
            won (bool): True if the player guessed the number correctly, False otherwise.
            attempts (int): The number of attempts used in the round.
            score (int): The score earned in the round.
        """
        # Using assignment operators to update stats
        self.games_played += 1
        self.total_attempts += attempts
        self.total_score += score
        
        # Storing score in the array data structure
        self.score_history.append(score)

        # Conditional statement to track win/loss count
        if won:
            self.games_won += 1
        else:
            self.games_lost += 1

    def get_win_percentage(self):
        """
        Calculates and returns the player's win rate as a percentage.
        Demonstrates arithmetic operators, type conversion, and division.
        """
        if self.games_played == 0:
            return 0.0
        
        # Win rate = (games won / total games) * 100
        win_rate = (self.games_won / self.games_played) * 100.0
        return round(win_rate, 1)

    def get_average_attempts(self):
        """
        Calculates the average number of attempts made per game.
        """
        if self.games_played == 0:
            return 0.0
        
        avg_attempts = self.total_attempts / self.games_played
        return round(avg_attempts, 1)
