def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    amount = get_number_of_words(text)
    print(amount)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(text):
    amount = 0
    for word in text.split():
        amount += 1
    return amount

main()