def word_count(text):
    word_list = text.split()
    return len(word_list)

def char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def dict_sort(char_count_dict):
    chars_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            char_dict = {"char": char, "count": count}
            chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_by_count)
    return chars_list

def sort_by_count(char_dict):
    return char_dict["count"]