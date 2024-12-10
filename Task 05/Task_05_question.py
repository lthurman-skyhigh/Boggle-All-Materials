from typing import List
from Task_05_helpers import get_word_path, print_board

"""
"highlight_word_on_board" returns the same board with the word highlighted in uppercase letters (if possible) by:
    1. Making a function call to "get_word_path" to find the path of the word on the board
    2. Returning the same board if no path is returned from "get_word_path"
    3. Declaring a new empty "highlighted_board" (a 4x4 2D-array, where all values are set to "None")
    4. Iterating over each square in "highlighted_board", and re-assigning it to the lowercase or uppercase letter for 
       the corresponding square in the (original) board, depending if the square's co-ordinates are in the returned "get_word_path"
    5. Returning "highlighted_board"
"""
def highlight_word_on_board(board: List[List[str]], word: str) -> List[List[str]]:
    #your code here
    return board

if __name__ == "__main__":
    TEST_BOARD = [['b', 'r', 'm', 'o'],
                  ['c', 'o', 'n', 't'],
                  ['i', 'g', 'l', 's'],
                  ['j', 'g', 'm', 'e'],]

    print_board(highlight_word_on_board(TEST_BOARD, "skyhigh")) #returns the same board because there is no path for "skyhigh"
    print_board(highlight_word_on_board(TEST_BOARD, "boggle")) #returns the board with capitalized letters at positions: (0,0), (1,1), (2,1), (2,2) (3,1), (3,3)  
    print_board(TEST_BOARD) #the original board should ALWAYS remain the same no matter what

    #(tip!: Add more test cases in order to improve the confidence of your solutions!) 