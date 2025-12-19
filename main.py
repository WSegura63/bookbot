import sys

def get_book_text(bookpath):
    with open(bookpath) as f:
        return f.read()
    
def main():
    print(f"Usage: python3 main.py <path_to_book>")
    if len(sys.argv) < 2:
        sys.exit(1)
    bookpath = sys.argv[1]
    print("============ BOOKBOT ============")
    ## bookpath = "books/frankenstein.txt"
    print(f"Analyzing book found at {bookpath}...")
    print("--------- Word Count ---------")
    book_text = get_book_text(bookpath)
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count ---------")
    unsorted_list = get_num_characters(book_text)
    sorted_items = sorted_list(unsorted_list)
    for char, count in sorted_items:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

from stats import get_num_words 
from stats import get_num_characters
from stats import sorted_list
main()