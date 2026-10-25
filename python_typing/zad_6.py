def a(l1: list, l2: list) -> list:
    s = set(l1 + l2)
    w = [i**3 for i in s]
    return w


print(a([1, 2, 3], [3, 4, 5]))
