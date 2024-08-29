def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    amount = get_number_of_words(text)
    character_count = each_character_used(text)
    sorted_characters = sort_characters_by_amount(character_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{amount} words found in the document")
    for dict in sorted_characters:
        character = dict["character"]
        value = dict["value"]
        print(f"The '{character}' character was found {value} times")
    print("--- End report ---")

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

def sort_characters_by_amount(characters):
    characters_list = []
    ## Convert to list of dictionaries
    for character in characters:
        if character.isalpha():
            temp = {}
            temp["character"] = character
            temp["value"] = characters[character]
            characters_list.append(temp)
    ## Sorts
    characters_list.sort(key=sort_on, reverse=True) 
    return characters_list

def sort_on(dict):
    return dict["value"]

main()