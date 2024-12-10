import time

def valid_word_solution(word: str):
    contains_a_vowel = False
    vowels = ["a", "e", "i", "o", "u", "y"]

    for letter in word:

        if not 97<=ord(letter)<=122:
            return False
            
        if letter in vowels:
            contains_a_vowel = True
        
    return len(word) >= 3 and contains_a_vowel


def word_in_list_solution(guessed_word: str, list_of_words: list[str], score: int):
    found = False

    for word in list_of_words:
        if guessed_word == word:
            found = True
    
    if found:
        score += len(guessed_word)

    else:
        print(f"The word '{guessed_word}' is not in the list")

    return score

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
    test_valid_word(valid_word_solution)
    test_word_in_list(word_in_list_solution)

    print("All tests passed! Well Done! :D")