# Project Statement: Number Guessing Game

## 1. Problem Statement
In introductory computer science curricula, students need practical projects that reinforce foundational programming concepts—such as variables, data structures, conditional control flow, loops, functions, and modular design—without overwhelming them with external libraries or graphic-heavy environments. 

The **Number Guessing Game** solves this pedagogical need by providing an engaging, interactive, console-based game where a player attempts to deduce a randomly generated secret integer within a set number of attempts. The system provides real-time comparative feedback ("Too high", "Too low", or "Correct"), tracks player performance across rounds, dynamically calculates scores, and maintains cumulative gameplay statistics.

---

## 2. Project Scope
The scope of this project is strictly tailored for a first-year B.Tech Computer Science and Engineering (CSE) student undertaking a **Python Essentials** course:

- **Environment**: Pure Command-Line Interface (CLI) execution using standard Python 3.
- **Dependencies**: Exclusively utilizes the Python Standard Library (built-in `random` and `array` modules). No third-party packages, web frameworks, graphical toolkits, or external databases are used.
- **Data Persistence**: In-memory session tracking for the player's session profile (games played, games won, games lost, average attempts, total score, and score history).
- **Architecture**: Modular separation of concerns across 7 distinct Python files (`main.py`, `game.py`, `player.py`, `difficulty.py`, `statistics.py`, `utilities.py`, and `tests.py`).

---

## 3. Target Users
- **Primary Users**: First-year engineering students, beginners learning Python, and casual command-line gamers looking for an interactive logic game.
- **Evaluators & Instructors**: Course instructors, teaching assistants, and viva examiners reviewing clean, readable, well-commented code that strictly mirrors the course syllabus.

---

## 4. High-Level Features
1. **Interactive Player Setup**: Personalized gameplay session with custom player name intake.
2. **Configurable Difficulty Levels**:
   - **Easy**: Range 1 to 50 | 10 maximum attempts.
   - **Medium**: Range 1 to 100 | 7 maximum attempts.
   - **Hard**: Range 1 to 200 | 5 maximum attempts.
3. **Randomized Secret Number Generation**: Cryptographically sound pseudorandom integer generation via Python's built-in `random.randint`.
4. **Intelligent Gameplay Feedback & History**:
   - Directional clues: "Too high" and "Too low".
   - Guess history tracking: lists previously tried numbers to prevent duplicate attempts.
   - Bitwise parity hint: reveals if the secret number is even or odd when attempts run low using binary bitwise operations.
5. **Linear Scoring Model**: Clear scoring formula rewarding players for fewer attempts:
   $$\text{score} = 100 - (\text{attempts\_used} - 1) \times 10 \quad (\text{minimum } 10 \text{ on win, } 0 \text{ on loss})$$
6. **Cumulative Player Statistics**: Real-time tracking of total games, win rate percentage, average attempts, and score histories via array structures.
7. **Comprehensive Standalone Validation**: Zero-dependency automated test runner (`tests.py`) verifying core algorithms, configuration mappings, and object state transitions.
