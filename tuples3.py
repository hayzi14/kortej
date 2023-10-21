def sieve(Q):
    p = []
    [p.append(item) for item in reversed(Q) if item not in p]
    return tuple(p)
print(sieve([7, 4, 1, 2, 8, 7]))
print(sieve([4, 1, 7, 3, 2, 4, 5, 1, 9, 0]))
print(sieve((1, 3, 7, 5, 1, 8, 2, 4, 6, 9)))
print(sieve((2, 5, 2, 10, 4, 1, 3, 12,)))
