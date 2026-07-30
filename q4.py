def is_vowel(char):
    vowels = 'aeiou'
    return char.lower() in vowels


def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()
        else:
            print("Please enter a single alphabetic character.")


text = get_valid_input('Enter a single alphabetic character: ')
if is_vowel(text):
    print(f"{text} is a vowel.")
else:
    print(f"{text} is not a vowel.")
