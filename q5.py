user_input = input('Enter a string: ')
vowel = ['a', 'e', 'i', 'o', 'u']


def translate(prompt):
    result = ""
    for i in range(len(prompt)):
        if prompt[i] in vowel:
            result += prompt[i]
        elif prompt[i] == " ":
            result += prompt[i] + " " + prompt[i]
        else:
            result += prompt[i] + "o" + prompt[i]

    return result


print(translate(user_input))


# TODO: FEEDBACK: we should not use 'string' as variable we have python's string module
#  which will be override if use string as variable (import string)
