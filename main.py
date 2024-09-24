def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = count_words(text)
    characters = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words found in the document")
    print()

    for item in chars_sorted_list: 
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for characters in text:
        if characters.lower() not in chars:
            chars[characters.lower()] = 1
        chars[characters.lower()] += 1
    return chars



main()
