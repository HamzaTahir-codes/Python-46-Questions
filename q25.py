def present_participle(verb):
    if verb.endswith('e') and not verb.endswith(('be', 'see', 'flee', 'knee')):
        return verb[:-1] + "ing"
    elif verb.endswith('ie'):
        return verb[:-2] + 'ying'
    elif len(verb) >= 3 and verb[-3] not in 'aeiou' and verb[-2] in 'aeiou' and verb[-1] not in 'aeiou' and verb[
        -1] not in 'sxz':
        return verb + verb[-1] + 'ing'
    else:
        return verb + "ing"


words = ["move", "see", "lie", "hug"]
for word in words:
    print(present_participle(word))
