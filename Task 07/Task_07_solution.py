import json
from typing import List
from Task_07_helpers import get_file_path

#Tests can cover:
#1. File exists, contains board and score, score >= current -> file unchanged
#2. File exists, contains board and score, score < current -> update file
#3. File doesn't exist -> update file

def set_highest_board_score(current_board: List[List[str]], current_board_max_score: int) -> None:
    highest_board_score_json_file = get_file_path("HighestBoardScore.json")
    highest_board = current_board
    highest_board_max_score = current_board_max_score

    try:
        with open(highest_board_score_json_file, "r") as file:
            saved_board = json.load(file)
            if saved_board["max_score"] >= highest_board_max_score:
                highest_board = saved_board["board"]
                highest_board_max_score = saved_board["max_score"]
    except FileNotFoundError:
        print("File not found, so we set the current board as the highest.")

    with open(highest_board_score_json_file, "w") as file:
        json.dump({
            "board": highest_board,
            "max_score": highest_board_max_score
        }, file)

if __name__ == "__main__":
    TEST_BOARD = [["o", "a", "h", "f"],
                  ["w", "o", "r", "s"],
                  ["r", "a", "r", "t"],
                  ["i", "d", "n", "s"]], 
    
    TEST_BOARD_MAX_SCORE = 770

    set_highest_board_score(TEST_BOARD, TEST_BOARD_MAX_SCORE) #should update HighestBoardScore.json with the TEST board + max_score (assuming it's not been edited)

    #(tip!: Don't forget to revert the file after each test using the comments in the helper file!)