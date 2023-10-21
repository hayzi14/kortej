P = 0
Q = 1
def slicer(a, b):
    p = s = P  
    if b in a:
        p = a.index(b)
    if a.count(b) > 1:
        s = a.index(b, s + 1) + 1
    else:
        s = Q
    return a[p:s]
print(slicer((1, 2, 4), 10))
print(slicer((1, 4, 2, 6, 4, 6, 7, 8), 4))
print(slicer((1, 2, 3, 5, 1, 6, 3), 12))
