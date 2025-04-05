import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count
from stats import char_count
from stats import dict_sort
from stats import sort_by_count

def main():
    text = get_book_text(book_path)
    num_words = word_count(text)
    counts_dict = char_count(text)
    char_sorted = dict_sort(counts_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in char_sorted:
        print(f"{char_dict['char']}: {char_dict['count']}")

main()