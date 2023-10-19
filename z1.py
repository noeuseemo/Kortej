def tpl_sort(a):
    for z in a:
        if not isinstance(z, int):
            return ()
    return tuple(sorted(a))
print (tpl_sort((4, 6, 3, 1, 8)))
print (tpl_sort((9, 6, 4, 2, 10)))
