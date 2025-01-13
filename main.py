def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_characters = get_count_characters(text)
    char_list = [{"char": key, "num": value} for key, value in count_characters.items()]
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print ()
    filtered_char_list = [char for char in char_list if char["char"].isalpha()]
    filtered_char_list.sort(reverse=True, key=sort_on)
    for i in filtered_char_list:
        print(f"The '{i['char']}' character was found {i['num']} times")
    print("--- End report ---")

def sort_on(filtered_char_list):
    return filtered_char_list["num"]


def get_count_characters(text):
    dictionary = {}
    for i in text:
        c = i.lower()
        if c in dictionary:
            dictionary[c] += 1 
        else: dictionary[c] = 1
    return dictionary
    

def get_num_words(text):
    words = text.split()
    #print (words)
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()