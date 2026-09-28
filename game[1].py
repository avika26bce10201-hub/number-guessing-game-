"""
game.py
-------
This module contains the core NumberGuessingGame class.
It handles target number generation, guess evaluations, attempt tracking,
and the execution of game rounds.
"""

import random
from statistics import calculate_score
from utilities import print_divider


class NumberGuessingGame:
    """
    Class encapsulating the mechanics of a single number guessing round.
    """

    def __init__(self, difficulty_name, number_range, max_attempts):
        """
        Initializes game state for a new round.

        Parameters:
            difficulty_name (str): Label for the chosen difficulty (e.g. 'Easy').
            number_range (tuple): Tuple of (low, high) defining the range.
            max_attempts (int): Maximum number of guesses permitted.
        """
        self.difficulty_name = difficulty_name
        self.low = number_range[0]
        self.high = number_range[1]
        self.max_attempts = max_attempts

        # Generate a random target number using built-in random module
        self.target_number = random.randint(self.low, self.high)
        
        # State tracking
        self.attempts_used = 0
        self.is_won = False
        self.guessed_numbers = []  # List to store sequence of guesses
        self.unique_guesses = set()  # Set to track unique numbers guessed

    def get_parity_hint(self):
        """
        Uses bitwise AND operator (&) to check if the target number is even or odd.
        In binary, (n & 1) isolates the least significant bit (0 = Even, 1 = Odd).
        """
        if (self.target_number & 1) == 0:
            return "Even"
        else:
            return "Odd"

    def check_guess(self, guess):
        """
        Compares the player's guess against the secret target number.

        Parameters:
            guess (int): The integer guessed by the player.

        Returns:
            str: "Too low", "Too high", or "Correct".
        """
        # Demonstrating type() function and identity operator (is not)
        if type(guess) is not int:
            guess = int(guess)

        self.attempts_used += 1
        self.guessed_numbers.append(guess)
        self.unique_guesses.add(guess)

        if guess < self.target_number:
            return "Too low"
        elif guess > self.target_number:
            return "Too high"
        else:
            self.is_won = True
            return "Correct"

    def play_round(self):
        """
        Executes the interactive guessing loop for the round.

        Returns:
            tuple: (won: bool, attempts: int, score: int)
        """
        print_divider("-")
        print(f"Starting {self.difficulty_name} Mode!")
        print(f"I'm thinking of a number between {self.low} and {self.high}.")
        print(f"You have {self.max_attempts} attempts. Best of luck!")
        print_divider("-")

        # Guessing loop: continues while attempts remain and player has not won
        while self.attempts_used < self.max_attempts and not self.is_won:
            current_attempt = self.attempts_used + 1
            remaining = self.max_attempts - self.attempts_used

            print(f"\n[Attempt {current_attempt}/{self.max_attempts}] ({remaining} attempts remaining)")

            # Show previous guesses if any exist
            if len(self.guessed_numbers) > 0:
                print(f"Your previous guesses: {self.guessed_numbers}")

            # Helpful parity hint when 2 or fewer attempts remain
            if remaining <= 2:
                print(f"💡 HINT: The secret number is {self.get_parity_hint()}!")

            # Prompt for guess (assumed valid integer as per instructions)
            guess_str = input(f"Enter your guess ({self.low} - {self.high}): ")
            guess = int(guess_str)

            # Check if guess is outside the allowed range
            if guess < self.low or guess > self.high:
                print(f"Notice: {guess} is outside the range ({self.low} - {self.high})!")

            # Check if number was already guessed previously (using membership operator)
            if guess in self.unique_guesses:
                print(f"Note: You already tried {guess} earlier!")

            # Evaluate guess
            feedback = self.check_guess(guess)

            if feedback == "Correct":
                print(f"\n>>> BINGO! You guessed the secret number {self.target_number} correctly! <<<")
                print(f"Attempts used: {self.attempts_used}")
                break
            elif feedback == "Too low":
                print(f"-> {guess} is TOO LOW! Try a higher number.")
            else:
                print(f"-> {guess} is TOO HIGH! Try a lower number.")

        # Round conclusion if attempts are exhausted without a correct guess
        if not self.is_won:
            print(f"\n>>> OUT OF ATTEMPTS! <<<")
            print(f"Better luck next time! The secret number was: {self.target_number}")

        # Compute round score
        round_score = calculate_score(self.is_won, self.attempts_used, self.max_attempts)
        print(f"Round Score: {round_score}")
        print_divider("-")

        return self.is_won, self.attempts_used, round_score
