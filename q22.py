def rot13(message):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't',
           'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
           'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j',
           'x': 'k',
           'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
           'F': 'S',
           'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z',
           'N': 'A',
           'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H',
           'V': 'I',
           'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

    result = ""

    for i in message:
        if i in key:
            result += key[i]
        else:
            result += i
    return result


ciphertext = input("enter text to be encrypted: ")
ciphertext = rot13(ciphertext)
print(ciphertext)
plaintext = input("enter text to be decrypted: ")
plaintext = rot13(plaintext)
print(plaintext)