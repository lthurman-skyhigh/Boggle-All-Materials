from typing import List

"""
Prints a 2D board of letters in a formatted manner.

Parameters:
board (List[List[str]]): The 2D board of letters. Each item represents a letter in the board.

Returns:
None: The function does not return any value. It instead prints the board to the console.
"""


def print_board(board: List[List[str]]) -> None:
    for row in board:
        print()
        print("  ".join(row))
    print()