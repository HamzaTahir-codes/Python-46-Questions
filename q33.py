def semordnilap_recognizer(filename):
    with open(filename, 'r') as file:
        words = [word.strip() for word in file]
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i][::-1] == words[j]:
                    print("Semordnilap pair found:", words[i], words[j])


filename = input("Enter the file name: ")
semordnilap_recognizer(filename)
