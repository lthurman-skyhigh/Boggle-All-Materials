import random
from Task_04_helpers import print_board
from typing import List

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
    # This is the initial 4x4 board
    board = [
        ["_", "_", "_", "_"],
        ["_", "_", "_", "_"],
        ["_", "_", "_", "_"],
        ["_", "_", "_", "_"]
    ]

    # an array of all the numbers representing the dice indices
    unused_dice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    for i in range(4):
        for j in range(4):
            # Here we pick a random index from the unused_dice array
            current_number = random.choice(unused_dice)

            # Here we pick a random letter from the DICE array at index current_number
            random_letter = random.choice(DICE[current_number])

            # We add this letter to the board
            board[i][j] = random_letter

            # Finally we remove the number from the dice indices so the same die is not chosen twice
            unused_dice.remove(current_number)
    return board


if __name__ == "__main__":
    print_board(generate_board())
