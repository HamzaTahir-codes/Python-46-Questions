def translate(words, lexicon):
    translated_words = []

    for i in words:
        if i in lexicon:
            translated_words.append(lexicon[i])
        else:
            translated_words.append(i)
    return translated_words


lexicon = {
    "merry": "god",
    "christmas": "jul",
    "and": "och",
    "happy": "gott",
    "new": "nytt",
    "year": "ar"
}

phrase = ["merry", "christmas", "and", "happy", "new", "year"]
new = translate(phrase, lexicon)
print(new)
