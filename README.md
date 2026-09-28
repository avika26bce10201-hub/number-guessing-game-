# Number Guessing Game (Console Application)

A beginner-friendly, modular command-line project built for first-year B.Tech Computer Science and Engineering (CSE) students in an introductory **Python Essentials** course.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Objectives](#objectives)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Python Course Concepts Demonstrated](#python-course-concepts-demonstrated)
7. [Project Structure](#project-structure)
8. [Installation and Setup Instructions](#installation-and-setup-instructions)
9. [How to Run the Project](#how-to-run-the-project)
10. [How to Test the Project](#how-to-test-the-project)
11. [Example Gameplay Walkthrough](#example-gameplay-walkthrough)
12. [Future Enhancements](#future-enhancements)

---

## Project Overview
The **Number Guessing Game** is an educational, console-based game implemented in pure standard Python 3. The game generates a secret random number within a designated numerical boundary. The player must deduce the number within a limited number of guesses. With each attempt, the game offers immediate directional feedback—informing the player if their guess is "Too high" or "Too low". When attempts run scarce, the game reveals an intelligent bitwise parity hint (Even/Odd).

The program tracks attempts, computes a score based on efficiency, records overall player performance, and displays statistical summaries.

---

## Problem Statement
First-year computer science undergraduates often learn foundational programming constructs (such as variables, conditional branches, loops, data structures, and functions) in isolation. Without building an integrated project, students frequently struggle to see how these individual concepts cooperate to form a coherent software architecture.

This project addresses that gap by assembling these core concepts into an entertaining, modular, readable, and evaluatable project that requires no external libraries or complex tools.

---

## Objectives
- **Demonstrate Core Python Syntax**: Naturally incorporate variables, conditional logic, loops, operators, and basic OOP.
- **Enforce Modular Programming**: Decompose application responsibilities into discrete, maintainable files.
- **Develop Interactive CLI Logic**: Handle console input, output formatting, and input validation without external packages.
- **Ensure Testability**: Provide transparent, standalone unit-level test validation runnable via a simple terminal command.
- **Viva-Readiness**: Maintain clear, straightforward code with descriptive docstrings so the student can explain every line during viva evaluations.

---

## Features
- **Personalized Sessions**: Collects player names and greets users on startup.
- **Three Tiered Difficulty Modes**:
  - **Easy**: Range $1 - 50$, 10 attempts
  - **Medium**: Range $1 - 100$, 7 attempts
  - **Hard**: Range $1 - 200$, 5 attempts
- **Directional Hints**: Clear, instant guidance indicating whether to guess higher or lower.
- **Duplicate Guess Warning**: Remembers previously submitted guesses using sets and warns if a number was already tried.
- **Bitwise Parity Hint**: When 2 or fewer attempts remain, the game calculates and displays whether the secret number is Even or Odd using binary bitwise operations (`number & 1`).
- **Score Calculation**: Calculates score based on attempts used:
  $$\text{score} = 100 - (\text{attempts\_used} - 1) \times 10 \quad (\text{minimum 10 points for a win, 0 for a loss})$$
- **Comprehensive Statistics**: Displays total games, wins, losses, win rate percentage, average attempts per game, and stores round scores in an integer array.
- **Replayability**: Allows consecutive rounds without losing player session data.

---

## Technologies Used
- **Language**: Python 3 (Tested on Python 3.10+)
- **Standard Library Modules**:
  - `random`: For pseudorandom integer generation (`random.randint`).
  - `array`: For storing round score sequences in a typed array data structure (`array.array('i')`).
- **Third-Party Libraries**: **None** (Zero external dependencies).

---

## Python Course Concepts Demonstrated

This project adheres strictly to the first-year B.Tech CSE Python Essentials curriculum. Below is a direct mapping of how each concept is integrated:

| Topic / Concept | Where and How It Is Used in the Project |
| :--- | :--- |
| **Python Fundamentals** | Clean indentation, script structure, docstrings, and comments across all `.py` files. |
| **Input and Output** | `input()` for receiving user names, choices, and guesses; `print()` and f-strings for formatted output. |
| **Variables** | Storing scores, attempt counts, target numbers, bounds, and string choices. |
| **Type Conversion** | Converting raw string input into integers (`int(guess_str)`), and floats for calculations. |
| **`type()` Function** | Validating that guess parameters are integer types (`type(guess) is not int`) in `game.py`. |
| **Arithmetic Operators** | Addition (`+`), subtraction (`-`), multiplication (`*`), and float division (`/`) in `statistics.py` and `player.py`. |
| **Assignment Operators** | Simple assignment (`=`) and compound assignment (`+=`, `-=`) for stats updating in `player.py`. |
| **Comparison / Relational Operators** | Checking bounds and conditions: `==`, `!=`, `<`, `>`, `<=`, `>=`. |
| **Logical Operators (`and`, `or`, `not`)** | Compound conditions such as `while attempts_used < max_attempts and not is_won` in `game.py`. |
| **Membership Operators (`in`, `not in`)** | Validating menu inputs against collections: `if choice in valid_options` and `if guess in unique_guesses`. |
| **Identity Operators (`is`, `is not`)** | Checking against `None` and verifying types: `if invalid is None` and `if type(guess) is not int`. |
| **Bitwise Operators** | Bitwise AND (`& 1`) in `get_parity_hint()` to inspect the least significant bit (LSB) to determine if target is even or odd. |
| **Operator Precedence & Associativity** | Arithmetic and relational combinations: `score = maximum_score - (attempts_used - 1) * 10`. |
| **Lists** | `guessed_numbers = []` in `game.py` to record the sequence of guesses made by the player. |
| **Tuples** | Numerical ranges `(low, high)` and configuration values in `DIFFICULTY_CONFIG`. |
| **Sets** | `unique_guesses = set()` to track distinct numbers entered and warn against redundant guesses. |
| **Frozen Sets** | Immutable option sets in `utilities.py`: `MAIN_MENU_OPTIONS = frozenset(["1", "2", "3"])`. |
| **Dictionaries** | Configuration mapping in `difficulty.py`: keying menu choices to configuration tuples. |
| **Control Flow Statements** | `if`, `elif`, `else` branches for game feedback; `while` loops for game turns and menus; `break` to exit loops upon victory. |
| **Functions** | Modularity via functions with arguments, default parameters, and return statements across modules. |
| **Modules and Packages** | Modular imports between `main.py`, `game.py`, `player.py`, `difficulty.py`, `statistics.py`, and `utilities.py`. |
| **Array Data Structure** | Using `array.array('i')` in `player.py` to store integer histories of individual round scores. |
| **Object-Oriented Programming (OOP)**| `Player` class in `player.py` and `NumberGuessingGame` class in `game.py` featuring encapsulation, `__init__`, and instance methods. |

---

## Project Structure

```text
number-guessing-game/
│
├── main.py          # Program entry point, menu routing, and game loop orchestration
├── game.py          # NumberGuessingGame class, target selection, and round execution
├── player.py        # Player class storing profile, statistics, and score history array
├── difficulty.py    # Difficulty configurations, range tuples, and limit mappings
├── statistics.py    # Score formula calculations and formatted performance metrics
├── utilities.py     # Reusable console banners, dividers, and safe input validators
├── tests.py         # Standalone test suite validating all core functions
├── README.md        # Comprehensive project documentation
└── statement.md     # Problem statement, scope, target audience, and high-level features
```

### Module Responsibilities:
- **`main.py`**: Boots the program, instantiates the `Player` profile, displays the main navigation menu, controls game repetition, and terminates cleanly.
- **`game.py`**: Encapsulates round state, generates the secret integer using `random.randint`, collects user guesses, issues "Too high"/"Too low" feedback, and awards victory.
- **`player.py`**: Tracks cumulative performance (games played, won, lost, total attempts, win rate, and typed array score histories).
- **`difficulty.py`**: Centralizes Easy, Medium, and Hard configurations using dictionaries and tuples.
- **`statistics.py`**: Calculates the round score using an arithmetic deduction formula and renders statistical summaries.
- **`utilities.py`**: Centralizes recurring formatting tasks (headers, divider lines) and input validation using frozensets.
- **`tests.py`**: Validates functions and class behaviors using assertions, conditions, and pass/fail reports without third-party frameworks.

---

## Installation and Setup Instructions

### Prerequisites
- Python 3.8 or higher installed on your computer.
- No external packages or `pip install` commands are needed.

### Setup
1. Clone or download this project repository to your computer.
2. Open a terminal (Command Prompt, PowerShell, or Bash) and navigate to the project directory:
   ```bash
   cd number-guessing-game
   ```
3. Verify your Python installation:
   ```bash
   python --version
   ```

---

## How to Run the Project

Run the application directly from your terminal:

```bash
python main.py
```

Follow the interactive on-screen prompts:
1. Enter your name.
2. Choose **1** to play a game.
3. Select your desired difficulty (Easy / Medium / Hard).
4. Enter your guesses and follow the clues to find the secret number!
5. After finishing a round, choose whether to play again, review your cumulative stats, or exit.

---

## How to Test the Project

To execute the automated validation suite without installing any external tools:

```bash
python tests.py
```

### Expected Output:
```text
========================================
   RUNNING PROJECT VALIDATION TESTS     
========================================
Testing difficulty settings...
  [PASS] test_difficulty_settings
Testing score calculation...
  [PASS] test_score_calculation
Testing Player class...
  [PASS] test_player_class
Testing Game mechanics...
  [PASS] test_game_mechanics
========================================
Results: 4/4 test suites PASSED successfully.
========================================
```

---

## Example Gameplay Walkthrough

Below is a demonstration of an interactive session on Easy difficulty:

```text
==================================================
  WELCOME TO THE NUMBER GUESSING GAME!
==================================================
A Python Essentials Project by a First-Year B.Tech CSE Student
--------------------------------------------------
Please enter your name: Alex

Hello, Alex! Get ready to test your intuition.

--- MAIN MENU ---
1. Play Game
2. View Statistics
3. Exit
Select an option (1-3): 1

--- Select Difficulty Level ---
1. Easy   -> Range: 1 to 50  | Attempts: 10
2. Medium -> Range: 1 to 100 | Attempts: 7
3. Hard   -> Range: 1 to 200 | Attempts: 5
Choose difficulty (1/2/3): 1

--------------------------------------------------
Starting Easy Mode!
I'm thinking of a number between 1 and 50.
You have 10 attempts. Best of luck!
--------------------------------------------------

[Attempt 1/10] (10 attempts remaining)
Enter your guess (1 - 50): 25
-> 25 is TOO LOW! Try a higher number.

[Attempt 2/10] (9 attempts remaining)
Your previous guesses: [25]
Enter your guess (1 - 50): 38
-> 38 is TOO HIGH! Try a lower number.

[Attempt 3/10] (8 attempts remaining)
Your previous guesses: [25, 38]
Enter your guess (1 - 50): 32

>>> BINGO! You guessed the secret number 32 correctly! <<<
Attempts used: 3
Round Score: 80
--------------------------------------------------
Do you want to play again? (y/n): n

--- MAIN MENU ---
1. Play Game
2. View Statistics
3. Exit
Select an option (1-3): 2
==================================================
  PERFORMANCE STATISTICS FOR ALEX
==================================================
 Total Games Played  : 1
 Games Won           : 1
 Games Lost          : 0
 Win Percentage      : 100.0%
 Total Attempts Made : 3
 Average Attempts    : 3.0
 Total Accumulated Score: 80
--------------------------------------------------

--- MAIN MENU ---
1. Play Game
2. View Statistics
3. Exit
Select an option (1-3): 3
==================================================
  THANK YOU FOR PLAYING!
==================================================
Goodbye, Alex! Hope you enjoyed the game.
==================================================
  PERFORMANCE STATISTICS FOR ALEX
==================================================
 Total Games Played  : 1
 Games Won           : 1
 Games Lost          : 0
 Win Percentage      : 100.0%
 Total Attempts Made : 3
 Average Attempts    : 3.0
 Total Accumulated Score: 80
--------------------------------------------------
```

---

## Future Enhancements
Once the student advances to subsequent terms in the B.Tech CSE program, the following features can be added:
- **Persistent High Scores**: Storing player profiles and historical records permanently using file I/O or SQLite databases.
- **Custom Ranges**: Allowing the user to input custom minimum and maximum range parameters.
- **Graphical User Interface (GUI)**: Migrating the console interactions to desktop or web frontends using Tkinter or modern web frameworks.
- **Timed Mode**: Incorporating Python's `time` module to track the time taken per round in addition to attempts.
