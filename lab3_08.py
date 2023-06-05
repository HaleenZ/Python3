def find_longest_words(text):
    words = text.split()
    longest_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == longest_length]
    return longest_words


# Example usage
text = input("Enter a text: ")

longest_words = find_longest_words(text)
if longest_words:
    print("Longest word(s):")
    for word in longest_words:
        print(word)
