def mapping(num):
    list0 = []
    for i in num:
        list0.append(len(i))
    return list0


print(mapping(["Apple", "Banana", "Cherry"]))


def mapping2(num):
    return list(map(lambda x: len(str(x)), num))


print(mapping2(["Apple", "Banana", "Cherry"]))


def mapping3(num):
    return [len(i) for i in num]


print(mapping3(["Apple", "Banana", "Cherry"]))
