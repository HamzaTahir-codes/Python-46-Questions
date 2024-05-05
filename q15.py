def find_longest_word(words):
    maximum = [len(w) for w in words]
    return max(maximum)


word = ['apple', 'banana', 'cherry', 'kiwi']
length = find_longest_word(word)
print(length)
