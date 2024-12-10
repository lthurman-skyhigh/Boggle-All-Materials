import random
from typing import List

from Task_04_helpers import print_board

"""
Complete the function below

A boggle board is created by rolling 16 dice with letters on them as shown below

The dice should be randomly allocated to different locations on the 4x4 board

You can use the helper function to print out the board

You might want to use the random library!
"""

DICE = [
    ['a', 'e', 'a', 'n', 'e', 'g'],  # 1
    ['a', 'h', 's', 'p', 'c', 'o'],  # 2
    ['a', 's', 'p', 'f', 'f', 'k'],  # 3
    ['o', 'b', 'j', 'o', 'a', 'b'],  # 4
    ['i', 'o', 't', 'm', 'u', 'c'],  # 5
    ['r', 'y', 'v', 'd', 'e', 'l'],  # 6
    ['l', 'r', 'e', 'i', 'x', 'd'],  # 7
    ['e', 'i', 'u', 'n', 'e', 's'],  # 8
    ['w', 'n', 'g', 'e', 'e', 'h'],  # 9
    ['l', 'n', 'h', 'n', 'r', 'z'],  # 10
    ['t', 's', 't', 'i', 'y', 'd'],  # 11
    ['o', 'w', 't', 'o', 'a', 't'],  # 12
    ['e', 'r', 't', 't', 'y', 'l'],  # 13
    ['t', 'o', 'e', 's', 's', 'i'],  # 14
    ['t', 'e', 'r', 'w', 'h', 'v'],  # 15
    ['n', 'u', 'i', 'h', 'm', 'qu'],  # 16
]


def generate_board() -> List[List[str]]:
    # code here (remove the pass)
    pass


if __name__ == "__main__":
    print_board(generate_board())
