# Sudoku-Player

## The rule of sudoku
On a 9x9 grid, you should fill out the empty cells with the numbers 1-9 without repeating any number within the row, column, or 3x3 squares.

## How to play
* Open and run the file "play_game.py" to start the game window.
* Click an empty cell and type in number to fill it.
* If the filled number is correct, the cell turns grey; if the number is incorrect, the cell turns red.
* Once the sudoku is correctly finished, "You did it!" will appear on the upper half of the window.

## Inside the game
* A randomly-generated sudoku puzzle with an unique solution
* A mistake count at the upper right corner
* A timer that starts once the game window is open
* A "show solution" button that auto-complete the puzzle

## Notes:
* The project extensively used pygame library to build the interactive game page.
* As part of the game mechanism, the built-in sudoku solver uses backtracking method to solve any sudoku with high accurary
* Each time the game is opened, the sudoku puzzle is different and randomly generated.
