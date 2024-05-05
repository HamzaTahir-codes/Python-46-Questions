def find_longest_word(words):
    maximum = list(map(lambda x: len(x), words))
    return max(maximum)


print(find_longest_word(['Hamza', 'Abbasi', 'Iubisauniversity']))
