def make_3gs_words(verb):
    if verb.endswith("y"):
        return verb[:-1] + "ies"
    elif verb.endswith(("o", "ch", "s", "sh", "x", "z")):
        return verb[:-1] + "es"
    else:
        return verb + "s"


words = ["try", "brush", "run", "fry"]
for word in words:
    print(make_3gs_words(word))
