def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_words = file_contents.split()
        num_words = len(file_words)
        print(f" Found {num_words} total words")

count = {}
def get_letter_number(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_lower = file_contents.lower()
        file_words = list(file_lower)
        for letter in file_words:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        return(count)

def sort_on(items):
    return items["num"]

def sort_letters():
    new_dict_list = [
        {"char": name, "num": time}
        for name, time in count.items() if name.isalpha()
    ]
    new_dict_list.sort(reverse=True, key=sort_on)
    for letter in new_dict_list:
        print(f"{letter['char']}: {letter['num']}")
