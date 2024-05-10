def alternade(text, set_all_words):
    """ returns a tuple containing the two words that form the alternade
        or None if the word is not an alternade
    """
    list_a = []
    list_b = []
    text_length = len(text)

    if text_length % 2:
        text_length += 1
        text = text + " "
    for i in range(0, len(text), 2):
        list_a.append(text[i])
        list_b.append(text[i + 1])
    str_a = ''.join(list_a).strip()
    str_b = ''.join(list_b).strip()

    if str_a in set_all_words and str_b in set_all_words:
        return str_a, str_b
    return None


set_all_words = set(["ass", "bad", "or", "wit", "dog"])

print(alternade("board", set_all_words))
print(alternade("waists", set_all_words))
