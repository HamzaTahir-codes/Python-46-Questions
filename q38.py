def average_word_length(file_name):
    total_length = 0
    word_count = 0

    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                total_length += len(word)
                word_count += 1

    # Calculate the average word length
    if word_count == 0:
        return 0  # Avoid division by zero
    else:
        return total_length / word_count


file_name = input("Enter the name of the file: ")
avg_length = average_word_length(file_name)
print("Average word length:", avg_length)
