def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_list(char_count):
    items = list(char_count.items())
    items.sort(key=num_key_return, reverse=True)
    return items

def num_key_return(pair):
    return pair[1]