def del_from_tuple(q, p):
    Q = list(q)
    if p in q:
        Q.remove(p)
    return tuple(Q)
print(del_from_tuple((1, 4, 2), 2))
print(del_from_tuple((4, 9, 5, 2, 6), 2))
print(del_from_tuple((10, 3, 1, 7, 1, 2), 7))
print(del_from_tuple((1, 4, 5, 1, 0, 2), 4))
