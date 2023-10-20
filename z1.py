def tpl_sort(abv):
    for element in abv:
        if not isinstance(element, int):
            return ()
        return tuple(sorted(abv))
print(tpl_sort((4, 2, 1.9, 5, 8)))
print(tpl_sort((2, 3, 2.6, 7, 9)))
