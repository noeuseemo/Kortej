def del_from_tuple(a, b):
    qwe = list(a)
    if b in a:
        qwe.remove(b)
    return tuple(qwe)
print(del_from_tuple((3, 4, 6), 6))
print(del_from_tuple((4, 8, 6, 5, 7), 0))
print(del_from_tuple((2, 1, 9, 5, 7, 6), 7))
print(del_from_tuple((2, 0, 5, 13, 2, 0), 5))
