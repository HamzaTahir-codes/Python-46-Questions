from functools import reduce


def max_in_list(array):
    max_item = array[0]
    for i in array[1:]:
        if i > max_item:
            max_item = i
    return max_item


print(max_in_list([1, 2, 6, 9, 5, 80, 30, 40]))

# Directly using the reduce function

numbers = [20, 25, 35, 40, 80, 70, 75]
junk = reduce(lambda x, y: x if x > y else y, numbers)
print(junk)
