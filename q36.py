import re
from collections import Counter

def find_hapaxes(filename):
    # Read the text from the file
    with open(filename, 'r') as file:
        text = file.read()

    # Tokenize the text into words, ignoring punctuation and converting to lowercase
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the frequency of each word
    word_counts = Counter(words)

    # Filter out words that occur only once
    hapaxes = [word for word, count in word_counts.items() if count == 1]

    return hapaxes

# Example usage:
filename = input("Enter the file name: ")
hapaxes = find_hapaxes(filename)
print("Hapax legomena in the file:", hapaxes)
