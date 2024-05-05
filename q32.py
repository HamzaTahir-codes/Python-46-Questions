import re

def is_palindrome(phrase):
    clean_phrase = re.sub('[^a-zA-Z0-9]', '', phrase.lower())
    start, end = 0, len(clean_phrase) - 1

    while start < end:
        if clean_phrase[start] != clean_phrase[end]:
            return False
        start += 1
        end -= 1

    return True

def palindrome_recognizer(filename):
    with open(filename, 'r') as file:
        for line in file:
            if is_palindrome(line):
                print(f"Line '{line.strip()}' is a palindrome.")
            else:
                print(f"Line '{line.strip()}' is not a palindrome.")

filename = input("Enter the file name: ")
palindrome_recognizer(filename)
