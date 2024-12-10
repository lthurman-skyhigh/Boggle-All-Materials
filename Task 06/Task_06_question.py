from typing import List
import random
import time

"""
Implement a binary search to find a word within a sorted list of words

If the word is in the list return True and False if not
"""

def binary_search(word: str, word_list: List[str]) -> bool:
    # code here (remove pass)
    pass


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