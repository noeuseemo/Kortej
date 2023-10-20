A = 0
N = -1
def slicer(a, n):
    g = gg = A   
    if n in a:
        z = a.index(n)
    if a.count(n) > 1:
        gg = a.index(n, g + 1) + 1
    else:
        gg = N
    return a[g:gg]
print(slicer((3, 1, 4), 10))
print(slicer((2, 7, 3, 4, 7, 6, 6, 5), 8))
print(slicer((2, 3, 1, 8, 2, 4, 7), 10))
