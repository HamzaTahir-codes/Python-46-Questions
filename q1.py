def maximum(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 == num2:
        return "The numbers are same"
    else:
        return f"{num2} is greater than {num1}"


print(maximum(2, 3))
