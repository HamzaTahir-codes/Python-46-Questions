import time
import pyttsx3

# ICAO alphabet dictionary
d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
     'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
     'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
     'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
     'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
     'z': 'zulu'}


def speak_ICAO(text, word_pause=0.1, sentence_pause=0.2):
    engine = pyttsx3.init()
    # engine.setProperty('rate', 300)  # Speed of speech
    for char in text.lower():
        if char.isalpha():
            word = d[char]
            engine.say(word)
            engine.runAndWait()
            time.sleep(word_pause)
        elif char.isspace():
            time.sleep(sentence_pause)


# Example usage:
text_to_speak = input("Enter Text to be encoded: ")
speak_ICAO(text_to_speak, word_pause=0.1, sentence_pause=0.5)
