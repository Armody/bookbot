from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    amount = get_number_of_words(text)
    character_count = each_character_used(text)
    sorted_characters = sort_characters_by_amount(character_count)

    print_report(book_path, amount, sorted_characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, amount, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Fount {amount} total words")
    print("--------- Character Count -------")
    for dict in sorted_characters:
        if dict["character"].isalpha():
            print(f"{dict['character']}: {dict['value']} times")
    print("============= END ===============")

main()