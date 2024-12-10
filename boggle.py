from typing import List, Set, Tuple, Any
import os
import random
import time
import threading
import copy
import json, csv

DIRECTIONS = [(0,1), (0,-1), (1,0), (1,-1), (1,1), (-1,0), (-1,-1), (-1,1)]
ALL_WORDS = set()
ROW_COUNT = 4
COL_COUNT = 4

DICE = [
    ['a','e','a','n','e','g'],  #1
    ['a','h','s','p','c','o'],  #2
    ['a','s','p','f','f','k'],  #3
    ['o','b','j','o','a','b'],  #4
    ['i','o','t','m','u','c'],  #5
    ['r','y','v','d','e','l'],  #6
    ['l','r','e','i','x','d'],  #7
    ['e','i','u','n','e','s'],  #8
    ['w','n','g','e','e','h'],  #9
    ['l','n','h','n','r','z'],  #10
    ['t','s','t','i','y','d'],  #11
    ['o','w','t','o','a','t'],  #12
    ['e','r','t','t','y','l'],  #13
    ['t','o','e','s','s','i'],  #14
    ['t','e','r','w','h','v'],  #15
    ['n','u','i','h','m','qu'], #16
        ]

# Function to construct the full file path for reading or writing files
def get_file_path(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

# Puts all the words from the Collins Scrabble Words (2015) file into a global set ALL_WORDS
try:
    with open(get_file_path("Collins Scrabble Words (2015).txt"), 'r') as f:
        for line in f:
            word = line.strip().lower()
            vowels = {"a", "e", "i", "o", "u", "y"}
            if len(word) >= 3 and len(set(word)) != 1 and any(char in vowels for char in word):
                ALL_WORDS.add(word.lower())
except FileNotFoundError:
    print("The word file was not found. Please check the file path.")

###

class WordTree:
    def __init__(self):
        self.root = {}
        self.validated = set()

    def add_word(self, word):
        """Add a word to the Trie."""
        node = self.root
        i = 0
        while i < len(word):
            if word[i:i+2] == "qu":
                node = node.setdefault("qu", {})
                i += 2
            else:
                node = node.setdefault(word[i], {})
                i += 1
        node['*'] = True

    def find_words(self, board):
        """Find all valid words on the board."""
        def dfs(row, col, path, node, word):
            if not (0 <= row < 4) or not (0 <= col < 4) or (row, col) in path:
                return
            
            letter = board[row][col]
            
            # Handle the "qu" case
            if letter == "qu" and "qu" in node:
                path.add((row, col))
                node = node["qu"]
                word += "qu"
                if '*' in node and len(word) > 2:
                    self.validated.add(word)
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr != 0 or dc != 0:
                            dfs(row + dr, col + dc, path, node, word)
                path.remove((row, col))
                return
            
            if letter in node:
                path.add((row, col))
                node = node[letter]
                word += letter
                if '*' in node and len(word) > 2:
                    self.validated.add(word)
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr != 0 or dc != 0:
                            dfs(row + dr, col + dc, path, node, word)
                path.remove((row, col))
        
        for r in range(4):
            for c in range(4):
                dfs(r, c, set(), self.root, '')
        return self.validated

###

#Function for printing the board
def print_board(board):
    for row in board:
        print()
        print("  ".join(row))
    print()

#Function to generate a random board with 4-6 vowels in it
def generate_board() -> List[List[str]]:

    # This is the initial 4x4 board
    board = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
            ]
    
    # an array of all the numbers representing the dice indices
    dice_numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    for i in range(4):
        for j in range(4):

            # Here we pick a random index from the dice_numbers array 
            current_number = random.choice(dice_numbers)
            
            # Here we pick a random letter from the DICE array at index current_number
            random_letter = random.choice(DICE[current_number])

            #We add this letter to the board
            board[i][j] = random_letter

            # Finally we remove the number from the dice indices so the same die is not chosen twice
            dice_numbers.remove(current_number)

    return board

#Function which gives 1 path for how a specific word can be made in the board
def get_word_path(board: List[List[str]], word: str) -> List[Tuple[int, int]]:
    def adjust_word_for_qu(word: str) -> str:
        adjusted_word = ""
        i = 0
        while i < len(word):
            if word[i] == 'q' and i + 1 < len(word) and word[i + 1] == 'u':
                adjusted_word += 'qu'
                i += 2
            else:
                adjusted_word += word[i]
                i += 1
        return adjusted_word
    
    def backtrack(x, y, idx, path):
        if idx == len(word):
            return True
        if x < 0 or x >= 4 or y < 0 or y >= 4 or (x, y) in path:
            return False
        current_char = board[x][y]
        if current_char == 'q':
            current_char = 'qu'
        if word[idx:idx + len(current_char)] != current_char:
            return False
        path.append((x, y))
        for dx, dy in DIRECTIONS:
            if backtrack(x + dx, y + dy, idx + len(current_char), path):
                return True
        path.pop()
        return False
    
    word = adjust_word_for_qu(word)
    
    for i in range(4):
        for j in range(4):
            path = []
            if backtrack(i, j, 0, path):
                return path

#Function that returns a dictionary with its key being the word found and its value being the path taken to create said word
def get_word_paths(board: List[List[str]], found_words: List[str]) -> dict[str, List[Tuple[int, int]]]:
    word_paths = {}

    for word in found_words:
        path = get_word_path(board, word)
        if path:
            word_paths[word] = path

    return word_paths

# Function that sorts a dictionary by itd key
def sort_dictionary_by_key(found_words: dict[str, List[Tuple[int, int]]]) -> dict[str, List[Tuple[int, int]]]:
    sorted_dict = dict(sorted(found_words.items()))
    return sorted_dict

# Function that asks for player count and validates input
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

#Function that finds the maximum score given a list of possible words from a board
def find_max_score(list_of_words: List[str]) -> List[str]:
    max_score = 0

    for word in list_of_words:
        max_score += len(word)
    
    return max_score

#Function that compares the current board score with the highest score and saves it in a JSON file if necessary
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

    with open(get_file_path("HighestBoardScore.json"), "w") as file:
        json.dump({
            "board": highest_board,
            "max_score": highest_board_max_score
        }, file)

#Function that asks user for a name then validates it  
def ask_and_validate_player_name(existing_player_names: Set[str]) -> str: 
    current_player_number = len(existing_player_names) + 1
    while True:
        name = input(f"Player {current_player_number}, Enter name: ")
        if len(name.strip()) == 0:
            print("Name cannot be empty!")
        elif name in existing_player_names:
            print(f"{name} is already taken, please use a different one!")
        else:
            return name

#Function which checks whether a word is a valid guess or not
def valid_word(word: str) -> bool:
    contains_a_vowel = False
    vowels = ["a", "e", "i", "o", "u", "y"]

    for letter in word:

        if not 97<=ord(letter)<=122:
            return False
            
        if letter in vowels:
            contains_a_vowel = True
        
    return len(word) >=3 and contains_a_vowel

#Function which checks whether the guessed word is in the list of valid words
def word_in_list(guessed_word: str, list_of_words: Set[str], score: int, list_of_guessed_words: Set[str]) -> Tuple[str, int, Set[str]]:
    found = False

    for word in list_of_words:
        if guessed_word == word:
            found = True
            list_of_words.remove(guessed_word)
            list_of_guessed_words.add(guessed_word)
            break
    
    if found:
        score += len(guessed_word)
        return f"Correct! Your score is now {score}", score, list_of_guessed_words
    
    return f"The word {guessed_word} is not in the list of all possible words", score, list_of_guessed_words

#Function that displays all the guessed words
def show_all_guessed_words(guessed_words: Set[str]):
    print(f"\nThe words you have guessed are: \n{guessed_words}\n")

#Function that resets the screen to have only the board show
def clear_screen_and_print_board(board: List[List[str]]):
    clear_screen()
    print("To reset the screen type 'RESET DISPLAY', To see all of your guesses, type 'SHOW GUESSES' \n")
    print_board(board)

#Clears terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Function that displays all of the words which can be made in the current board
def print_all_possible_words(all_possible_words: set[str]):
    word_length_dict = {} #key = number, value = sorted list of words which have the length of that number
    for word in all_possible_words:
        word_length = len(word)
        if word_length not in word_length_dict:
            word_length_dict[word_length] = []
        word_length_dict[word_length].append(word)
    for key in word_length_dict:
        word_length_dict[key].sort()
    longest_word_length = max(word_length_dict.keys())

    print(f"\nThere are {len(all_possible_words)} possible words to be made. They are:")
    words_per_row = 15
    for word_length in range(longest_word_length, 0, -1):
        if word_length in word_length_dict:
            print(f"\nWords with {word_length} letters:")
            for i in range(0, len(word_length_dict[word_length]), words_per_row):
                print(', '.join(word_length_dict[word_length][i:i+words_per_row]))

#Function which prompts the user to ask how specific words would be made on the board
def ask_and_highlight_specific_words_on_board(board: List[List[str]], all_possible_words: set[str]):
    while True:
        word = input("\nWould you like to see how any specific word would be made on the board? Enter nothing otherwise: ")
        if not word:
            break
        elif not valid_word(word):
            print(f"{word} is invalid thus would never be made on the board!")
        elif word not in all_possible_words:
            print(f"{word} cannot be made on the board!")
        else:
            print(f"\n{word}:")
            print_board(highlight_word_on_board(board, word))

#Function that returns the same board with the word in question highlighted in underlined capitcal letters
def highlight_word_on_board(board: List[List[str]], word: str) -> List[List[str]]:
    word_path = get_word_path(board, word)
    if word_path == None:
        return board
    
    highlighted_board = []
    for row in range(4):
        highlighted_board.append([None] * 4)

    for row_index in range(4):
        for col_index in range(4):
            if (row_index, col_index) in word_path:
                highlighted_board[row_index][col_index] = board[row_index][col_index].upper()
            else:
                highlighted_board[row_index][col_index] = board[row_index][col_index]
    
    return highlighted_board

#Function that shows the leaderboard (top 10 players)
def show_leaderboard():
    players_with_scores = []

    with open(get_file_path("PlayersWithScores.csv"), "r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if row != ["Name", "Score"]:
                players_with_scores.append([row[0], float(row[1])])
    
    top_ten = (sort_by_scores(players_with_scores))

    print("\nTOP 10 PLAYERS:")

    for place, (name, score) in enumerate(top_ten):
        print(f"{place+1}: {name}, {score}%")
    
    print("\n")

#Function that shows the highest scoring boggle board (if it exists)
def show_highest_scoring_boggle_board():
    try:
        with open(get_file_path("HighestBoardScore.json"), "r") as file:
            saved_board = json.load(file)
            board_grid = saved_board["board"]
            saved_board_score = saved_board["score"]
            print("\nThe board we have recorded so far which yielded the highest score is shown below:")
            print_board(board_grid)
            print(f"\nIt has a maximum score of {saved_board_score}!\n")
    except FileNotFoundError:
        print("Board could not be found at this time.")


#Function that returns a message on how to play boggle
def how_to_play():
    message = """

    1. Find as many words as you can in the board that abide by the following rules:

        • Words must be at least three letters long.
        • The letters used to form a word must touch in sequence 
        horizontally, vertically, or diagonally in any direction.
        • Each letter can be used only once in a word.
        • Any word in any tense and any form (singular or plural) 
        is allowed as long as it can be found in an agreed English 
        dictionary.
        • Words within words are allowed. For example, if you find pear, 
        don't forget pea and ear.   
    
    2. Once you cannot find any more words, type "I GIVE UP" and your results will be shown
    
    """

    return message

#Function that takes as input a List[List[player, score]] and sorts the list according to the score and returns the top 10 scoring players
def sort_by_scores(players_with_scores: List[List[Any]]) -> List[List[Any]]:

    n = len(players_with_scores)
    for i in range(n):
        for j in range(n-i-1):
            if players_with_scores[j][1] < players_with_scores[j + 1][1]:
                players_with_scores[j], players_with_scores[j+1] = players_with_scores[j+1], players_with_scores[j]
    
    return players_with_scores[:10]

#Function that takes a List[List[player, score]] and adds this to the leaderboard+
def add_to_leaderboard(player_data):
    with open(get_file_path("PlayersWithScores.csv"), mode='a', newline='') as f:
        writer = csv.writer(f)
        for each_player in player_data:
            writer.writerow(each_player)

#Function that displays multiplayer results
def multiplayer_results(players_with_scores: List[List[Any]]):
    
    def get_ordinal(n):
        suffix = {
            1:"st",
            2:"nd",
            3:"rd",
        }

        return str(n)+suffix.get(n, "th")

    players_with_scores = sort_by_scores(players_with_scores)

    current_place = 1
    previous_score = None
    tie = False

    for name, score in players_with_scores:
        if previous_score == None:
            previous_score = score
        
        elif score == previous_score:
            tie = True

        else:
            current_place += 1
            previous_score = score
            tie = False
        
        print("In "+ ("tied " if tie else "") + f"{get_ordinal(current_place)} place was player {name} with a score of {score}")

#Function which will start the game
def menu():

    while True:
        clear_screen()
        user_choice = input("Boggle\n1.  How to play?\n2.  Singleplayer\n3.  Multiplayer\n4.  Leaderboard\n5.  Highest scoring board\n6.  Exit\n")
        if user_choice in {"1", "2", "3", "4", "5", "6"}:
            break
    
    if user_choice == "1":
        print(how_to_play())

    if user_choice == "2":
        print("Loading Singleplayer mode ...")
        load_game()
    
    elif user_choice == "3":
        number_of_players = ask_and_validate_player_count()
        print("Loading Multiplayer mode ...")
        load_game(number_of_players)

    elif user_choice == "4":
        show_leaderboard()

    elif user_choice == "5":
        show_highest_scoring_boggle_board()
    
    elif user_choice == "6":
        print("Thank you for playing!")
        exit()
    
    input("Press enter to go back to menu")
    clear_screen()
    menu()

def load_game(player_count=1):

    word_tree = WordTree()
    for word in ALL_WORDS:
        word_tree.add_word(word)

    # Generate board and find words using WordTree
    board = generate_board()
    word_tree.find_words(board)
    all_possible_words = word_tree.validated

    maximum_score = find_max_score(all_possible_words)
    set_highest_board_score(board, maximum_score)

    # Get paths for the validated words
    paths = sort_dictionary_by_key(get_word_paths(board, all_possible_words))

    print("Loaded\n")
    time.sleep(.5)

    if player_count > 1:
        names_already_taken = set()
        players_with_scores = []

        for player in range(1, player_count+1):
            name = ask_and_validate_player_name(names_already_taken)
            names_already_taken.add(name)
            name, score = play_game(board, all_possible_words, maximum_score, name)
            players_with_scores.append([name, score])
        
        multiplayer_results(players_with_scores)
        add_to_leaderboard(players_with_scores)

    else:
        name, score = play_game(board, all_possible_words, maximum_score)
        add_to_leaderboard([[name, score]])
    
    while True:
        show_user_all = input("Would you like to see all the words that are possible to make within this board?  (Y/N) ")
        if show_user_all in {"Y","N"}:
            break
    
    if show_user_all == "Y":
        print_all_possible_words(all_possible_words)
        ask_and_highlight_specific_words_on_board(board, all_possible_words)

def play_game(board: List[List[str]], all_words: set, max_score: int, name: str = None):

    if not name:
        name = input("Enter name  ")

    score = 0

    print_board(board)

    all_words_copy = all_words.copy()
    guessed_words = set()
    given_up = False

    print("To reset the screen type 'RESET DISPLAY', To see all of your guesses, type 'SHOW GUESSES'\n")

    while not given_up:
        new_guess = input("Guess a word or type 'I GIVE UP' to give up:   ")

        if new_guess == "I GIVE UP":
            given_up = True
        
        elif new_guess == "RESET DISPLAY":
            clear_screen_and_print_board(board)
        
        elif new_guess == "SHOW GUESSES":
            show_all_guessed_words(guessed_words)
        
        elif not valid_word(new_guess):
            print("Please enter a valid lowercase english word at least 3 letters long!")

        elif new_guess in guessed_words:
            print("You have already found this word!")

        else:
            message, score, guessed_words = (word_in_list(new_guess, all_words_copy, score, guessed_words))
            print(message)
        
        if score == max_score:
            print("You have found all of the words!")
            break
    
    player_percentage = 0 if max_score==0 else round((score/max_score)*100, 2)
    
    print(f"Well done {name}, You got {player_percentage}% of all the words possible in this board! Your score was {score} and the maximum score was {max_score}")

    return name, player_percentage

if __name__ == "__main__":
    menu()