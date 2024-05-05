def char_freq_table(filename):
    with open(filename, 'r') as file:
        content = file.read()
        freq_table = {}

        for char in content:
            if char.isalpha():
                char = char.lower()
                if char in freq_table:
                    freq_table[char] += 1
                else:
                    freq_table[char] = 1
        for char, freq in sorted(freq_table.items()):
            print(f"{char} : {freq}")


filename = input("Enter Filename:")
char_freq_table(filename)