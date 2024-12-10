from typing import Any
import time


"""
Complete the functions below

valid_word should check whether a word is:

1.  At least 3 letters long
2.  All lowercase
3.  Only characters from a-z
4.  Must contain at least one vowel. vowels are the letters: a, e, i, o, u, y

word_in_list should check whether the guessed word is in the list of words

    If the word is in the list, add the length of the word to the score variable and return the score

    If the word is not in the list, print a message saying: 
    
    "The word 'guessed_word' is not in list"

    And return the score
"""



def valid_word(word: str) -> bool:
    # code here (remove the pass)
    pass


def word_in_list(guessed_word: str, list_of_words: list[str], score: int) -> int:
    not_in_list_message = f"The word '{guessed_word}' is not in the list)"
    # code here (remove the pass)
    pass


#Testing your functions, please DO NOT CHANGE

def test_valid_word(function):
    TESTS = [("skyhigh", True), ("w0rld", False), ("This is a valid word", False), ("boggle", True), ("PROGRAMMING", False), (")&*$%&!$", False), ("validword", True), ("python", True), ("skhgh", False), ("crypt", True), ("hi", False)]

    print("Testing valid_word ... ")
    time.sleep(1)

    for word, result in TESTS:
        assert function(word) == result, f"\n\nYour function returned the wrong value. \n\nFor the word: {word}, the result should be: {result}. \nYour function returned: {function(word)}\n\n"
    
    print("All tests passed for valid_word ! :)")

def test_word_in_list(function):

    WORD_LIST = ["boggle", "skyhigh", "hello", "world", "test", "program", "python", "word"]
    WORD_TESTS_WITH_SCORE = [("boggle", 10), ("skyhigh", 42), ("pithon", 77), ("function", 44), ("world", 88), ("tester", 12)]
    ANSWERS = [16, 49, 77, 44, 93, 12]

    print("Testing word_in_list ... ")
    time.sleep(1)

    for i, (guessed_word, score) in enumerate(WORD_TESTS_WITH_SCORE):
        assert function(guessed_word, WORD_LIST, score) == ANSWERS[i], f"\n\nYour function returned the wrong value. \n\nThe result should be: {ANSWERS[i]}.\nYour function returned: {function(guessed_word, WORD_LIST, score)}\n\n"
    
    print("All tests passed for valid_word ! :)")

if __name__ == "__main__":
    test_valid_word(valid_word)
    test_word_in_list(word_in_list)

    print("All tests passed! Well Done! :D")