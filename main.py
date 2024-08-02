def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    generate_report(num_words, chars_dict, book_path)
  
def generate_report(num_words, chars_dict, book_path):
    dictlist = []
    for character, count in chars_dict.items():
        new_dict = {
            "character": character,
            "num": count
        }
        dictlist.append(new_dict)

    dictlist.sort(reverse=True, key=lambda d: d["num"])

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for entry in dictlist:
        character = entry["character"]
        num = entry["num"]
        print(f"The {character} character was found {num} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()
