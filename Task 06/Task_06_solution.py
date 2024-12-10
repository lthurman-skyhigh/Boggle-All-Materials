from typing import List
import random
import time

def binary_search(guessed_word: str, word_list: List[str]) -> bool:
    # Initialize the starting point (first) and ending point (last) of the list
    first = 0
    last = len(word_list) - 1
    found = False  # Flag to check if the guessed word is found

    # Loop until the search range is valid (first <= last) and the word is not found
    while first <= last and not found:
        # Find the middle index of the current range
        midpoint = (first + last) // 2
        
        # Check if the guessed word matches the word at the midpoint
        if word_list[midpoint] == guessed_word:
            found = True
        else:
            # If the guessed word is less than the midpoint word, search the left half
            if guessed_word < word_list[midpoint]:
                last = midpoint - 1
            else:
                # Otherwise, search the right half
                first = midpoint + 1
        
    return found

#Testing your functions, please DON'T CHANGE
if __name__ == "__main__":
    WORD_LIST = ['apple', 'banana', 'binary', 'break', 'bubble', 'cast','custom', 'dice', 'economy', 'equal', 'fast', 'feel', 'forward', 'fun', 'gobble', 'hit', 'instant', 'jump', 'kite', 'lake', 'laptop', 'loop', 'milton', 'mirage', 'money', 'notice', 'office', 'party', 'popular', 'program', 'python', 'quarantine', 'school', 'skyhigh', 'sort', 'space', 'super', 'symphony', 'tidy', 'upright', 'visual', 'voice', 'water', 'word', 'xylem', 'xylophone', 'zebra', 'zenith']
    WORD_TESTS = ['tidy', 'lime', 'food', 'mirage', 'instant', 'random', 'equal', 'dive', 'gobble']

    random.shuffle(WORD_TESTS)

    print("Testing binary_search ... ")

    time.sleep(1)

    for word in WORD_TESTS:
        assert binary_search(word, WORD_LIST) == (word in WORD_LIST), f"\n\nYour function returned the wrong value for the word '{word}'.\n" + ("This word is in the list" if word in WORD_LIST else "This word is not in the list") + "\n\n"
    
    print("All tests passed! Well done :D")