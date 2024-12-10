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
Make sure at the bottom, you add a new line!
Original content of PlayersWithScores.csv:

Name,Score
Umar,32.4
Louis,54.2
Ahmer,44.2
Bob,9.2
Dave,14.5
Steve,62.2
Jenkins,83.2
Daisy,39.4
Aliyah,22.4
Priyanka,47.2
Joanne,18.7
columbo,0.77


"""
