def filter_long_words(words, n):
    list1 = []
    for i in words:
        if len(i) > n:
            list1.append(i)
    return list1


def validate_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid integer.")


list0 = ["Apple", "Banana", "cherry"]
n = validate_input("Enter a number >>> ")
print(filter_long_words(list0, n))

# TODO: FEEDBACK: what if user enters some string value?
