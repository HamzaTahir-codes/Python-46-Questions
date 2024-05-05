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


phrase = input('Enter phrase to check: ')
print(is_palindrome(phrase))
