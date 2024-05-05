def pangram(phrase):
    phrase = phrase.lower()

    alphabets = set("abcdefghijklmnopqrstuvwxyz")

    return set(phrase) >= set(alphabets)


print(pangram("The quick brown fox jumps over the lazy dog"))
