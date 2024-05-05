def char_freq(string):
    frequency = {}

    for i in string:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency


print(char_freq("abbabbabbcbbabbabbabbabb"))
