from collections import Counter


def sort_on(char_dict):
    return char_dict["num"]


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")

    words = file_contents.lower().split()
    words_number = len(words)
    print(f"{words_number} words found in the document")

    text = file_contents.lower()
    conteo = Counter(text)

    character_counts = [
        {"char": char, "num": count}
        for char, count in conteo.items()
        if char.isalpha()
    ]

    character_counts.sort(reverse=True, key=sort_on)

    for item in character_counts:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
