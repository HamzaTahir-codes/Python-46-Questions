def filter_long_words(words, n):
    return [i for i in words if len(i) > n]


word = ['apple', 'banana', 'cherry', 'kiwi']
length = int(input('Enter length of word: '))
print(filter_long_words(word, length))

