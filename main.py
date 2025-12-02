import sys

from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_character_count_dictionaries

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_books_text(sys.argv[1])
    word_count = get_word_count(text)

    char_count = get_character_count(text)

    sorted_char_count_dicts = get_sorted_character_count_dictionaries(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words in the book.")
    print("--------- Character Count -------")
    for entry in sorted_char_count_dicts:
       print(f"{entry['char']}: {entry['num']}")


def get_books_text(filepath):
    with open(filepath) as f:
        return f.read()

main()