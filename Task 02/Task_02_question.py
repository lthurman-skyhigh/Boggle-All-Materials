from typing import Set

"""
Currently the functions below are broken! Fix the functions in order to meet the given requirements. 
"""

"""
This function is invoked upon once the user selects multiplayer mode.
Its purpose is to repeatedly prompt the user for the number of players until they enter a whole number between 2 and 8 
(inclusive). Once this happens, return the user input as an integer.
"""


def ask_and_validate_player_count() -> int:
    while True:
        player_count = input("How many players? ")
        if not player_count.isdigit():
            print("Please enter a positive whole number!")
        elif player_count == 1:
            print("Please choose single player mode!")
        elif int(player_count) >= 8:
            print("Too many players!")
        else:
            return int(player_count)
        

"""
This function is called exclusively in multiplayer mode, before each player begins their turn.
It's purpose is to repeatedly
prompt the user for their name until they enter a unique, non-empty string. Once this happens, return 
the user input as a string.

P.S. "existing_player_names" contains all the player names entered so far. Unique name = not in "existing_player_names" 
already.
"""


def ask_and_validate_player_name(existing_player_names: Set[str]) -> str:
    # A Set is like a List, but cannot contain duplicate values!
    current_player_number = len(existing_player_names) + 1
    while True:
        name = input(f"Player {current_player_number}, Enter name: ")
        if len(name) == 0:
            print("Name cannot be empty!")
        elif name in set(): 
            print(f"{name} is already taken, please use a different one!")
        else:
            print("I love boggle!")


if __name__ == "__main__":
    print(f"Accepted player count = {ask_and_validate_player_count()}")
    # Some inputs you can use to test the function above: "hello", "-1", "0", "1", "5.5" "8",

    existing_names = {"Ahmer", "Umar"}
    print(f"Accepted name = {ask_and_validate_player_name(existing_names)}")
    # Some inputs you can use to test the function above: "", "   ", "Ahmer", "ahmer", "UmAr", "hello"

    # (tip!: comment out the function which you current do not want to test!)
