from typing import List
from Task_05_helpers import get_word_path, print_board

def highlight_word_on_board(board: List[List[str]], word: str) -> List[List[str]]:
    word_path = get_word_path(board, word)
    if word_path == None:
        return board
    
    highlighted_board = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]

    for row_index in range(4):
        for col_index in range(4):
            if (row_index, col_index) in word_path:
                highlighted_board[row_index][col_index] = board[row_index][col_index].upper()
            else:
                highlighted_board[row_index][col_index] = board[row_index][col_index]
    
    return highlighted_board

if __name__ == "__main__":
    TEST_BOARD = [['b', 'r', 'm', 'o'],
                  ['c', 'o', 'n', 't'],
                  ['i', 'g', 'l', 's'],
                  ['j', 'g', 'm', 'e'],]
    
    print_board(highlight_word_on_board(TEST_BOARD, "skyhigh")) #returns the same board because there is no path for "skyhigh"
    print_board(highlight_word_on_board(TEST_BOARD, "boggle")) #returns the board with capitalized letters at positions: (0,0), (1,1), (2,1), (2,2) (3,1), (3,3) 
    print_board(TEST_BOARD) #the original board should ALWAYS remain the same no matter what