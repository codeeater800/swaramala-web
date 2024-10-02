import csv
import json

# Load dictionary data from CSV file
def load_dictionary():
    words = []
    with open('data/sanskrit_dictionary.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            words.append(row[0].strip())
    return words

# Simple search functionality
def simple_search(input_word, dictionary):
    matches = [entry for entry in dictionary if input_word in entry]
    return matches, len(matches)

# Complex search using syllables
def complex_search(target_syllable, position=None, search_type='position', word_map_file='data/sanskrit_word_map.json'):
    with open(word_map_file, 'r', encoding='utf-8') as json_file:
        word_map = json.load(json_file)

    results = []
    for original_word, split_word in word_map.items():
        split_syllables = split_word.split()

        if search_type == 'position' and len(split_syllables) > position and split_syllables[position] == target_syllable:
            results.append(original_word)
        elif search_type == 'end' and split_syllables[-1] == target_syllable:
            results.append(original_word)

    return results[:10]
