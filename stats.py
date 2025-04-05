def get_book_text(filepath):
    with open(filepath) as f:

        file_to_string = f.read()
        words = file_to_string.split()

        print("Found", len(words), "total words")


def get_char(filepath):
    with open(filepath) as f:

        characters = {}
        file_as_string = f.read()

        lower_string = file_as_string.lower()
        
        for char in lower_string:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

        return characters

def sorted(filepath):

    def sort_on(character_list):
        return character_list["count"]
    
    with open(filepath) as f:
        string = f.read()
        lower_string = string.lower()

        characters = {}


        for char in lower_string:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1


        character_list = []

        for char in characters:
            character_list.append({'char': char, 'count': characters[char]})

        
        character_list.sort(reverse=True, key=sort_on)

        return character_list



def report(filepath):
    
    char_counted_sorted = sorted(filepath)

    char_final = []

    for char_dict in char_counted_sorted:
        if char_dict['char'].isalpha():
            char_final.append(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_book_text(filepath)
    print("--------- Character Count -------")
    for char_dict in char_final:
        print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

    


#sorted("books/frankenstein.txt")
#report("books/frankenstein.txt")

