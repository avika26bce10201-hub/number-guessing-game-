"""
main.py
-------
Main entry point for the Number Guessing Game.
Orchestrates player setup, main menu navigation, game loop execution,
and program termination.
"""

from player import Player
from difficulty import display_difficulty_menu, get_difficulty_settings
from game import NumberGuessingGame
from statistics import display_player_stats
from utilities import (
    print_header,
    print_divider,
    get_menu_choice,
    MAIN_MENU_OPTIONS,
    DIFFICULTY_OPTIONS,
    CONFIRMATION_OPTIONS
)


def display_main_menu():
    """
    Displays the primary navigation menu.
    """
    print("\n--- MAIN MENU ---")
    print("1. Play Game")
    print("2. View Statistics")
    print("3. Exit")


def play_game_flow(player):
    """
    Handles difficulty selection and initiates a game round for the player.
    Demonstrates module interactions, function calls, and object updates.
    """
    display_difficulty_menu()
    
    # Validate difficulty choice using valid options from utilities
    difficulty_choice = get_menu_choice("Choose difficulty (1/2/3): ", DIFFICULTY_OPTIONS)
    print()  # Visual spacing
    settings = get_difficulty_settings(difficulty_choice)

    # Initialize a new game round object
    game_round = NumberGuessingGame(
        difficulty_name=settings["name"],
        number_range=settings["range"],
        max_attempts=settings["max_attempts"]
    )

    # Play the round
    won, attempts, score = game_round.play_round()

    # Update player profile statistics
    player.record_game(won, attempts, score)


def main():
    """
    Main function to run the Number Guessing Game.
    """
    print_header("Welcome to the Number Guessing Game!")
    print("A Python Essentials Project by a First-Year B.Tech CSE Student")
    print_divider("-")

    # Prompt for player name
    player_name = input("Please enter your name: ").strip()
    if player_name == "":
        player_name = "Player 1"

    # Instantiate player object
    player = Player(player_name)
    print(f"\nHello, {player.name}! Get ready to test your intuition.")

    # Program loop
    is_running = True
    while is_running:
        display_main_menu()
        menu_choice = get_menu_choice("Select an option (1-3): ", MAIN_MENU_OPTIONS)

        if menu_choice == "1":
            # Play one or more rounds
            keep_playing = True
            while keep_playing:
                play_game_flow(player)
                
                # Ask if player wants to play another round immediately
                play_again_input = get_menu_choice("Do you want to play again? (y/n): ", CONFIRMATION_OPTIONS)
                if play_again_input in ("n", "N"):
                    keep_playing = False

        elif menu_choice == "2":
            # View player statistics
            display_player_stats(player)

        elif menu_choice == "3":
            # Exit program
            print_header("Thank You for Playing!")
            print(f"Goodbye, {player.name}! Hope you enjoyed the game.")
            display_player_stats(player)
            is_running = False


# Standard Python pattern to execute main() when run as a script
if __name__ == "__main__":
    main()
