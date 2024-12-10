def menu():
    message = "Boggle\n1.  How to play?\n2.  Singleplayer\n3.  Multiplayer\n4.  Leaderboard\n5.  Highest scoring board\n6.  Exit\n"
    user_choice = input(message)

    if user_choice == "1":
        how_to_play()

    elif user_choice == "2":
        single_player()
    
    elif user_choice == "3":
        multi_player()

    elif user_choice == "4":
        show_leaderboard()

    elif user_choice == "5":
        show_highest_scoring_boggle_board()
    
    elif user_choice == "6":
        print("Thank you for playing!")
        exit()

    else:
        print("Invalid input")


def how_to_play():
    print("This is how to play ...")


def single_player():
    print("Loading single player mode ...")


def multi_player():
    print("Loading multi player mode ...")


def show_leaderboard():
    print("Loading leaderboard ...")


def show_highest_scoring_boggle_board():
    print("Loading Highest scoring board ...")


if __name__ == "__main__":
    menu()
