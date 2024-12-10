import os

"""
This function constructs an absolute file path based on the given filename.
It uses the current file's directory as the base path.

Parameters:
filename (str): The name of the file for which the absolute path is required.

Returns:
str: The absolute path of the specified file.
"""
def get_file_path(filename: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

"""
Original content of HighestBoardScore.json:

{"board": [["u", "h", "e", "k"], ["s", "h", "e", "b"], ["i", "r", "t", "w"], ["o", "s", "h", "r"]], "max_score": 690}

"""