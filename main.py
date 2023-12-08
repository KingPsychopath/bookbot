def main():
    path_to_file = 'books/frankenstein.txt'
    text = get_book_text(path_to_file)
    character = 'p'

    # print(text)
    print(f'Total Number of Words in Corpus: {count_total_words(text)}')
    print(f'Occurences of the letter {character} : {count_single_char(text, character)}')
    print(f'Occurences of each character: {get_character_dict(text)}')
    print(f'Report: {print_report(text)}')

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        return(f.read())

def count_total_words(text):
    return(len(text.split()))

def count_single_char(text, target_char):
    counter = 0
    #text = text.replace(' ', '') # Only removes space's, not tabs, new lines or other forms of white space.
    text = ''.join(text.split())
    for character in text:
        if character.lower() == target_char.lower():
            counter += 1
    return counter

def get_character_dict(text):
    # from collections import defaultdict 
    # counter = defaultdict(int) 
    # Could use a defaultdict instead of counter.get to define default value of missing keys in the mapping
    counter = {}

    text = ''.join(text.lower().split())
    for character in text:
        counter[character] = counter.get(character, 0) + 1
    return counter

def print_report(text):
    character_dictionary = get_character_dict(text) # Get the dictionary of characters and their occurrence count
    character_list = list(filter(lambda char: char[0].isalpha(), character_dictionary.items())) # Filter out non-alphabetic characters
    character_list.sort(key=lambda char: char[1], reverse=True)  # Sort the list in descending order based on occurrence count
    for character_set in character_list:
        print(f"The '{character_set[0]}' character was found {character_set[1]} times")
    return '--- Finished Printing Report! ---'


main()