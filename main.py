def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_char_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print_char_count(num_char)
    print("--- End report ---")

def sort_on(dict): 
    return dict["count"]

def print_char_count(dict): # Sort character count by most used and filter out non-letters
    dict_list = []
    for char in dict:
        dict_list.append({"character": char, "count": dict[char]}) #add non-alphas to list in case we want to count them later
    dict_list.sort(reverse=True, key=sort_on)
    for i in dict_list:
        if not i["character"].isalpha(): # If character is non-alpha don't print just continue the loop
            continue
        print(f"The {i['character']} character was found {i['count']} times")


def get_char_count(text): # Counts the number of times each character appears in text.
    lowered_text = text.lower()
    character_counts = {}
    for x in list(lowered_text):
        if x in character_counts:
            character_counts[x] += 1
        else:
            character_counts[x] = 1
    return character_counts


def get_num_words(text): # Splits the text at white space (" ") and returns the number of words.
    words = text.split()
    return len(words)


def get_book_text(path): # Opens file and stores the text as a string.
    with open(path) as f:
        return f.read()


main()