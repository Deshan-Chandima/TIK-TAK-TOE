🎲 Tic-Tac-Toe (Python Console Game)

A simple Tic-Tac-Toe game built with Python.
Two players (X and O) can play against each other in the terminal.



📌 How to Play

The game board has 9 positions arranged like this:

1 | 2 | 3
4 | 5 | 6
7 | 8 | 9


Player X always starts first.

On your turn, enter a number (1–9) to place your symbol on the board.

You cannot overwrite an existing move.

The game ends when:

A player gets 3 in a row (horizontal, vertical, or diagonal).

OR the board is full → Tie.

📂 Files

Main.py → Game code

README.md → Documentation



▶️ Run the Game

Install Python 3. Check version:

python --version


or

python3 --version


Run the game:

python Main.py

🎮 Example Gameplay
- | - | -
- | - | -
- | - | -

X's turn.
Choose a position from 1-9: 5

- | - | -
- | X | -
- | - | -

O's turn.
Choose a position from 1-9: 1

O | - | -
- | X | -
- | - | -




✅ Features

Two-player mode (X vs O).

Detects wins and ties.

Simple command-line interface.