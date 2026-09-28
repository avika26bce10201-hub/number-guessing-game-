"""
tests.py
--------
Simple test script to validate core game functions and models.
Note: In accordance with course constraints, this script does NOT use external
testing frameworks (such as unittest or pytest). It uses simple function calls,
conditions, and print statements.
"""

from difficulty import get_difficulty_settings
from statistics import calculate_score
from player import Player
from game import NumberGuessingGame


def test_difficulty_settings():
    """Validates difficulty configuration mappings and boundary values."""
    print("Testing difficulty settings...")
    
    easy = get_difficulty_settings("1")
    assert easy["name"] == "Easy", f"Expected Easy, got {easy['name']}"
    assert easy["range"] == (1, 50), f"Expected (1, 50), got {easy['range']}"
    assert easy["max_attempts"] == 10, f"Expected 10, got {easy['max_attempts']}"

    medium = get_difficulty_settings("2")
    assert medium["name"] == "Medium", f"Expected Medium, got {medium['name']}"
    assert medium["range"] == (1, 100), f"Expected (1, 100), got {medium['range']}"
    assert medium["max_attempts"] == 7, f"Expected 7, got {medium['max_attempts']}"

    hard = get_difficulty_settings("3")
    assert hard["name"] == "Hard", f"Expected Hard, got {hard['name']}"
    assert hard["range"] == (1, 200), f"Expected (1, 200), got {hard['range']}"
    assert hard["max_attempts"] == 5, f"Expected 5, got {hard['max_attempts']}"

    invalid = get_difficulty_settings("99")
    assert invalid is None, f"Expected None for invalid choice, got {invalid}"

    print("  [PASS] test_difficulty_settings")


def test_score_calculation():
    """Validates score formula logic for wins and losses."""
    print("Testing score calculation...")

    # Won on 1st attempt: 100 - (1 - 1) * 10 = 100
    score_1st = calculate_score(won=True, attempts_used=1, max_attempts=10)
    assert score_1st == 100, f"Expected 100, got {score_1st}"

    # Won on 3rd attempt: 100 - (3 - 1) * 10 = 80
    score_3rd = calculate_score(won=True, attempts_used=3, max_attempts=10)
    assert score_3rd == 80, f"Expected 80, got {score_3rd}"

    # Won on 10th attempt: 100 - (10 - 1) * 10 = 10
    score_10th = calculate_score(won=True, attempts_used=10, max_attempts=10)
    assert score_10th == 10, f"Expected 10, got {score_10th}"

    # Lost game: score must be 0 regardless of attempts
    score_lost = calculate_score(won=False, attempts_used=10, max_attempts=10)
    assert score_lost == 0, f"Expected 0 for loss, got {score_lost}"

    print("  [PASS] test_score_calculation")


def test_player_class():
    """Validates Player class initialization, stats updating, and win rate calculation."""
    print("Testing Player class...")

    player = Player("Aarav")
    assert player.name == "Aarav"
    assert player.games_played == 0
    assert player.games_won == 0
    assert player.games_lost == 0
    assert player.total_attempts == 0
    assert player.total_score == 0
    assert player.get_win_percentage() == 0.0

    # Record first game (Win in 4 attempts with score 70)
    player.record_game(won=True, attempts=4, score=70)
    assert player.games_played == 1
    assert player.games_won == 1
    assert player.games_lost == 0
    assert player.total_attempts == 4
    assert player.total_score == 70
    assert player.get_win_percentage() == 100.0
    assert player.get_average_attempts() == 4.0

    # Record second game (Loss with 6 attempts with score 0)
    player.record_game(won=False, attempts=6, score=0)
    assert player.games_played == 2
    assert player.games_won == 1
    assert player.games_lost == 1
    assert player.total_attempts == 10
    assert player.total_score == 70
    assert player.get_win_percentage() == 50.0
    assert player.get_average_attempts() == 5.0

    # Test score_history using Python's built-in array data structure
    assert len(player.score_history) == 2, f"Expected 2 recorded scores in array, got {len(player.score_history)}"
    assert player.score_history[0] == 70, f"Expected first score 70, got {player.score_history[0]}"
    assert player.score_history[1] == 0, f"Expected second score 0, got {player.score_history[1]}"

    print("  [PASS] test_player_class")


def test_game_mechanics():
    """Validates target evaluation logic, bitwise parity hint, and state transitions."""
    print("Testing Game mechanics...")

    game = NumberGuessingGame("Easy", (1, 50), 10)
    # Set deterministic target number for controlled testing
    game.target_number = 25

    # Test bitwise parity hint: 25 is odd (25 & 1 == 1)
    assert game.get_parity_hint() == "Odd", f"Expected Odd for 25, got {game.get_parity_hint()}"
    game.target_number = 24
    assert game.get_parity_hint() == "Even", f"Expected Even for 24, got {game.get_parity_hint()}"
    game.target_number = 25  # Reset to 25

    # Test guess below target
    feedback_low = game.check_guess(15)
    assert feedback_low == "Too low", f"Expected 'Too low', got '{feedback_low}'"
    assert game.attempts_used == 1
    assert not game.is_won
    assert 15 in game.guessed_numbers
    assert 15 in game.unique_guesses

    # Test guess above target
    feedback_high = game.check_guess(40)
    assert feedback_high == "Too high", f"Expected 'Too high', got '{feedback_high}'"
    assert game.attempts_used == 2
    assert not game.is_won
    assert 40 in game.guessed_numbers
    assert 40 in game.unique_guesses

    # Test correct guess
    feedback_correct = game.check_guess(25)
    assert feedback_correct == "Correct", f"Expected 'Correct', got '{feedback_correct}'"
    assert game.attempts_used == 3
    assert game.is_won
    assert 25 in game.guessed_numbers
    assert 25 in game.unique_guesses

    print("  [PASS] test_game_mechanics")


def run_all_tests():
    """Runs all test suites sequentially and prints summary."""
    print("========================================")
    print("   RUNNING PROJECT VALIDATION TESTS     ")
    print("========================================")
    
    test_functions = [
        test_difficulty_settings,
        test_score_calculation,
        test_player_class,
        test_game_mechanics
    ]

    passed = 0
    total = len(test_functions)

    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except Exception as error:
            print(f"  [FAIL] {test_func.__name__}: {error}")

    print("========================================")
    print(f"Results: {passed}/{total} test suites PASSED successfully.")
    print("========================================")


if __name__ == "__main__":
    run_all_tests()
