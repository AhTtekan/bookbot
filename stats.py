def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    result = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result

def sort_on(items):
    return items["num"]

def get_sorted_character_count_dictionaries(char_count_dictionary):
    result = []
    for char, count in char_count_dictionary.items():
        result.append({"char": char, "num": count})
    result.sort(reverse=True, key=sort_on)
    return result