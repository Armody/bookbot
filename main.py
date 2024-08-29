def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    amount = get_number_of_words(text)
    character_count = each_character_used(text)
    print(amount)
    print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(text):
    amount = 0
    for word in text.split():
        amount += 1
    return amount

def each_character_used(text):
    character_count = {}
    for character in text.lower():
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count

main()