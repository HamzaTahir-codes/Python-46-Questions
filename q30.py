lexicon = {
    "merry": "god",
    "christmas": "jul",
    "and": "och",
    "happy": "gott",
    "new": "nytt",
    "year": "ar"
}


def translate(words, lexicon):

    translated = list(map(lambda x: lexicon.get(x, words), words))
    return translated


message = ["merry", "christmas", "and", "happy", "new", "year"]
print(translate(message, lexicon))
