import csv
from Task_09_helpers import get_file_path
from typing import List, Tuple

"""
Complete the 2 functions below

The function add_to_leaderboard will take as parameter player_data which is a List[List[name: str, score: float]]

You will need to write the player scores and names to the PlayersWithScores.csv file 

The function sort_by_scores will take as parameter players_with_scores which is a List[List[name: str, score: float]]

You will need to sort the list in descending order using bubble sort

Then return the first 10 elements of the list using list slicing

"""

def add_to_leaderboard(player_data: List[Tuple[str, float]]):
    # code here (remove pass)
    pass

def sort_by_scores(players_with_scores: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    # code here (remove pass)
    pass

def show_leaderboard():
    players_with_scores = []

    with open(get_file_path("PlayersWithScores.csv"), "r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if row != ["Name", "Score"]:
                players_with_scores.append([row[0], float(row[1])])
    

    # Your function will be used here!
    top_ten = (sort_by_scores(players_with_scores))

    print("\nTOP 10 PLAYERS:")

    for place, (name, score) in enumerate(top_ten):
        print(f"{place+1}: {name}, {score}%")
    
    print("\n")

if __name__ == "__main__":

    print("Testing add_to_leaderboard...")

    try:
        add_to_leaderboard([['Ron', 31]])
        add_to_leaderboard([['Robert', 12], ['Tim', 5.2], ["Barbra", 4.13]])
    
    except Exception as e:
        print(f"An error occurred {e}")

    print("No errors found, Please check csv file to see if new players with scores have been added!\n")

    print("Testing sort_by_scores...")

    show_leaderboard()