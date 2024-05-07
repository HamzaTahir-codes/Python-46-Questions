def max_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"{num1} is greater than {num2} and {num3}"
    elif num2 > num1 and num2 > num3:
        return f"{num2} is greater than {num1} and {num3}"
    else:
        return f"{num3} is greater than {num1} and {num2}"


def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid number")


num1 = get_valid_input("Enter Number 1: ")
num2 = get_valid_input("Enter number 2: ")
num3 = get_valid_input("Enter number 3: ")

print(max_of_three(num1, num2, num3))
# print(max_of_three(12,30,11)


