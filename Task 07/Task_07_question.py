import json
from typing import List
from Task_07_helpers import get_file_path

"""
"set_highest_board_score" compares the contents of the current board to the one stored in "HighestBoardScore.json".
If the maximum possible score from the current board is higher than the stored score, it updates "HighestBoardScore.json" 
with the current board and score.

In programming we must not assume anything unless explicitly stated! "HighestBoardScore.json" may not exist, in which case 
you must create a new "HighestBoardScore.json" to include the current board.

You may assume the following ONLY:
1. current_board and current_board_max_score always contain valid values
2. If "HighestBoardScore.json" does exist, it will always contain valid values for "board" and "score"

Complete the function below: the path of the file in question has already been obtained
"""
def set_highest_board_score(current_board: List[List[str]], current_board_max_score: int) -> None:
    highest_board_score_json_file = get_file_path("HighestBoardScore.json")
    #your code here

if __name__ == "__main__":
    TEST_BOARD = [["o", "a", "h", "f"],
                  ["w", "o", "r", "s"],
                  ["r", "a", "r", "t"],
                  ["i", "d", "n", "s"]], 
    
    TEST_BOARD_MAX_SCORE = 770

    set_highest_board_score(TEST_BOARD, TEST_BOARD_MAX_SCORE) #should update HighestBoardScore.json with the TEST board + max_score (assuming it's not been edited)

    #(tip!: Don't forget to revert the file after each test using the comments in the helper file!)