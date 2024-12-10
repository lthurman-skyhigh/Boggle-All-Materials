from typing import Set


def ask_and_validate_player_count() -> int:
    while True:
        player_count = input("How many players? ")
        if not player_count.isdigit() or int(player_count) <= 0:
            print("Please enter a positive whole number!")
        elif int(player_count) == 1:
            print("Please choose single player mode!")
        elif int(player_count) > 8:
            print("Too many players!")
        else:
            return int(player_count)


def ask_and_validate_player_name(existing_player_names: Set[str]) -> str:
    # A Set is like a List, but cannot contain duplicate values!
    current_player_number = len(existing_player_names) + 1
    while True:
        name = input(f"Player {current_player_number}, Enter name: ")
        if len(name.strip()) == 0:
            print("Name cannot be empty!")
        elif name in existing_player_names:
            print(f"{name} is already taken, please use a different one!")
        else:
            return name


if __name__ == "__main__":
    print(f"Accepted player count = {ask_and_validate_player_count()}")
    # Some inputs you can use to test the function above: "hello", "-1", "0", "1", "5.5" "8",

    existing_names = {"Ahmer", "Umar"}
    print(f"Accepted name = {ask_and_validate_player_name(existing_names)}")
    # Some inputs you can use to test the function above: "", "   ", "Ahmer", "ahmer", "UmAr", "hello"

    # (tip!: comment out the function which you current do not want to test!)
