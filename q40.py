import random


def pick_word():
    colour_words = ['black', 'blue', 'brown', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow']
    return random.choice(colour_words)


def permute_words(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


def play_angram():
    original_word = pick_word()
    angram = permute_words(original_word)

    print("The angram word is:", angram)

    while True:
        guess = input("Guess a word: ")

        if guess.lower() == original_word:
            print("Correct!")
            break
        else:
            print("Wrong! Try Again")


play_angram()
