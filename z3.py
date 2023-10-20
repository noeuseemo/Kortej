def sieve(qwe):
    a = []
    [a.append(item) for item in reversed(qwe) if item not in a]
    return tuple(a)
print(sieve([2, 1, 4, 1, 7, 6]))
print(sieve([0, 5, 6, 3, 4, 5, 6, 2, 8, 0]))
print(sieve((2, 1, 6, 10, 3, 7, 5, 6, 4, 7)))
print(sieve((3, 1, 9, 5, 10, 5, 4, 11,)))
