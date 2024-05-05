import re


def split_sentences(text):
    # Regular Expression use
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'

    sentences = re.split(pattern, text)

    return sentences


def main():
    with open("test33.txt", "r") as file:
        text = file.read()

    sentences = split_sentences(text)

    for sentence in sentences:
        print(sentence)


main()
