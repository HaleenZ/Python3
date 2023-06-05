import re
from collections import Counter

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            words = re.findall(r'\w+', file.read().lower())
            word_count = Counter(words)
            return word_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")


# Example usage
file_path = input("Enter the path of the file: ")

word_frequency = count_word_frequency(file_path)
if word_frequency:
    print("Word frequency:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")
