def map1(f, l):
    new = []
    for i in l:
        new.append(f(i))
    return new


def filter1(f, l):
    new = []
    for i in l:
        if f(i):
            new.append(i)
    return new


def reduce1(f, l):
    new = l[0]
    for i in l[1:]:
        new = f(new, i)
    return new


print(reduce1(max, [1, 2, -45, 3, 0]))
print(map1(lambda x: x * 2, [1, 2, 3, 4]))
print(filter1(lambda x: x.endswith('in'), ('lapin', 'cretin', 'ah', 'oui')))
