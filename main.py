def main():
    # Defining Book Path
    frankenstein = "books/frankenstein.txt"

    # Calling read_book
    book_text = read_book(frankenstein)

    # Calling count_words
    total_words = count_words(book_text)
    print(f"There are {total_words} total words in the text")

    # Calling count_chars
    total_chars = count_chars(book_text)
    
    main_sorted_list = sort_dict(total_chars)
    
    for item in main_sorted_list:
        if not item["char"].isalpha():
            continue
        else: 
            print(f"The '{item['char']}' character was found '{item['num']}' times")

# Takes a path and outputs a string of text
def read_book(path):
    with open(path) as f:
        return f.read()

# Takes a string and outputs word count
def count_words(input):
    split_text = input.split()
    return len(split_text)

# Takes a string and outputs count of each char
def count_chars(input):
    lower_text = input.lower()
    char_dict = {}

    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

# Define Sort Key
def sort_on(input):
    return input["num"]

# Sorts dictionary based on key
def sort_dict(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

       
main()

