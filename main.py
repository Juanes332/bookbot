import sys
from stats import get_num_words, count_characters, sort_character_counts


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print(f"{get_num_words(text)} words found in the document")

    char_counts = count_characters(text)
    sorted_chars = sort_character_counts(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()
