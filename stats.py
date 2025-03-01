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
        characters_list.append({"character": character, "value": characters[character]})
    ## Sorts
    characters_list.sort(key=sort_on, reverse=True) 
    return characters_list

def sort_on(dict):
    return dict["value"]