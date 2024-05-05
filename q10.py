def overlapping(over, array):
    for i in array:
        for j in over:
            if i == j:
                return True
    return False


print(overlapping([1, 2, 3], [4, 5, 6]))
