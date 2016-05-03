def SortingFun(g):
    s = lambda a: sum([ord(k)-97 for k in a])
    m = lambda a, b: s(a) - s(b)
    return sorted (g, cmp=m)

print SortingFun(["Denise", "Tim", "Jennifer"])
