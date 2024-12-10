def print_all_possible_words(all_possible_words: set[str]) -> None:
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


if __name__ == "__main__":
    WORDS = {
    'apple', 'banana', 'cactus', 'daisy', 'elephant', 'fig', 'grape', 
    'hat', 'igloo', 'jacket', 'kite', 'lamp', 'monkey', 'nose', 'octopus',
    'piano', 'quilt', 'rose', 'star', 'taco', 'umbrella', 'violin', 
    'whale', 'xylophone', 'yacht', 'zebra', 'cat', 'dog', 'rat', 'bat',
    'mat', 'pat', 'tap', 'fog', 'log', 'not', 'lot', 'pot', 'cot', 'dot',
    'fan', 'can', 'pan', 'ran', 'man', 'van', 'tan', 'bag', 'tag', 'lag',
    'bag', 'tag', 'rat', 'sat', 'fat', 'dog', 'hot', 'bot', 'zip', 'tip',
    'rib', 'lip', 'soup', 'tree', 'rain', 'hand', 'play', 'game', 'rock',
    'ball', 'read', 'link', 'time', 'shot', 'seat', 'mask', 'pear', 'seal',
    'milk', 'beef', 'fish', 'pork', 'veal', 'flat', 'bowl', 'cake', 'roll',
    'bake', 'juice', 'fruit', 'salad', 'crepe', 'candy', 'sugar', 'flour',
    'bread', 'cheese', 'whisk', 'knife', 'plate', 'spoon', 'salad', 'bacon',
    'carrot', 'celery', 'pepper', 'spinach', 'eggplant', 'squash', 'pumpkin',
    'broccoli', 'chicken', 'onion', 'tomato', 'potato', 'cabbage', 'fennel',
    'chili', 'sorbet', 'icecream', 'cream', 'yogurt', 'lobster', 'crab',
    'clam', 'squid', 'mussel', 'oyster', 'salmon', 'tuna', 'pizza', 
    'burrito', 'sushi', 'rice', 'cereal', 'quinoa', 'oatmeal', 'barley',
    'millet', 'corn', 'cactus', 'ocean', 'moon', 'star', 'sky', 'tree',
    'house', 'car', 'bike', 'road', 'field', 'lake', 'mountain', 'cloud',
    'desert', 'forest', 'river', 'valley', 'wind', 'fire', 'earth', 
    'water', 'dawn', 'dusk', 'sunset', 'sunrise', 'beach', 'city', 'town'
    }
    NON_SIX_LETTER_WORDS = set(filter(lambda word: len(word) != 6, WORDS))

    #print_all_possible_words(WORDS)
    print_all_possible_words(NON_SIX_LETTER_WORDS) #should be no mention of 6-letter words in the output