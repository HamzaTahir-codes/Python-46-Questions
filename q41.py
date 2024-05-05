import random


def generate_hidden_word():
    words = ['apple', 'banana', 'cherry', 'lemon', 'orange', 'peach', 'pear', 'strawberry', 'watermelon']
    return random.choice(words)


def give_clue(hidden_word, guess):
    clue = ''
    for i in range(len(guess)-1):
        if guess[i] == hidden_word[i]:
            clue += '[' + guess[i] + ']'
        else:
            clue += guess[i]

    # Check for correct characters in wrong position
    for i in range(len(guess)):
        if guess[i] != hidden_word[i] and guess[i] in hidden_word:
            clue = clue.replace(guess[i], '(' + guess[i] + ')', 1)

    return clue


def play_lingo():
    hidden_word = generate_hidden_word()
    print("Welcome to Lingo! Try to guess the hidden word.")
    print(f"Hint: It is a {len(hidden_word)} letter word.")

    while True:
        guess = input("Enter your guess: ").lower()

        clue = give_clue(hidden_word, guess)
        print("Clue:", clue)

        if guess == hidden_word:
            print("Congratulations! You guessed the hidden word:", hidden_word)
            break


play_lingo()
