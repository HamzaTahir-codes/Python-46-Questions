def max_in_list(array):
    max_item = array[0]
    for i in array[1:]:
        if i > max_item:
            max_item = i
    return max_item


print(max_in_list([1, 2, 6, 9, 5, 80, 30, 40]))
