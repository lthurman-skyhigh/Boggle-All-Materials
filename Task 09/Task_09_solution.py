import csv
from typing import List, Tuple
from Task_09_helpers import get_file_path

def add_to_leaderboard(player_data: List[Tuple[str, float]]):
    # Open the 'PlayersWithScores.csv' file in append mode ('a')
    # 'newline=""' ensures that no extra blank lines are added in the file
    with open(get_file_path("PlayersWithScores.csv"), mode='a', newline='') as f:
        writer = csv.writer(f)  # Create a CSV writer
        for each_player in player_data:  # Iterate through the player data list
            writer.writerow(each_player)  # Write each player's data as a new row in the CSV file


def sort_by_scores(players_with_scores: List[Tuple[str, float]]) -> List[Tuple[str, float]]:

    n = len(players_with_scores)  # Get the number of players

    for i in range(n):  # Outer loop to go through the list multiple times
        for j in range(n - i - 1):  # Inner loop to compare adjacent scores

            # If the current score is less than the next score, swap them
            if players_with_scores[j][1] < players_with_scores[j + 1][1]:
                players_with_scores[j], players_with_scores[j + 1] = players_with_scores[j + 1], players_with_scores[j]
    
    return players_with_scores[:10]  # Return the top 10 players based on score

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
