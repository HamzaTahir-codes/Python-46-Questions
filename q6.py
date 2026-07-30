def sum_of_numbers(val):
    val1 = 0
    for i in val:
        val1 += i
    return val1


def multiply_numbers(val):
    val2 = 1
    for i in val:
        val2 *= i
    return val2


num_list = [1, 2, 3, 4]
print(sum_of_numbers(num_list))
print(multiply_numbers(num_list))

