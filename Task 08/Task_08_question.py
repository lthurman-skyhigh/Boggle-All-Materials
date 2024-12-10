def print_all_possible_words(all_possible_words: set[str]) -> None:
    for word in all_possible_words:
        print(word)


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
    NON_SIX_LETTER_WORDS = filter(lambda word: len(word) != 6, WORDS)

    #print_all_possible_words(WORDS)
    print_all_possible_words(NON_SIX_LETTER_WORDS) #should be no mention of 6-letter words in the output