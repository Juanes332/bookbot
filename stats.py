def get_num_words(text):
    return len(text.split())


def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_character_counts(char_dict):
    sorted_chars = [{"char": char, "num": count}
                    for char, count in char_dict.items() if char.isalpha()]
    sorted_chars.sort(key=lambda x: x["num"], reverse=True)
    return sorted_chars
