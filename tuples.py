def tpl_sort(p):
    for q in p:
        if not isinstance(q, int):
            return ()
    return tuple(sorted(p))
print(tpl_sort((9, 1, 4, 2, 7)))
print(tpl_sort((5, 8, 1, 3, 11)))
