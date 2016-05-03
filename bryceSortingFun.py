import sys

def SortingFun(group):
    s = "abcdefghijklmnopqrstuvwxyz"
    q = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    g = []
    g.extend([0]*len(group))
    #convert names into numbers
    for i in range(0,len(group)):
        for j in range(0,len(group[i])):
            for k in range(0,len(s)):
                if s[k] == str(group[i][j]) or  q[k] == str(group[i][j]):
                    g[i] += k

    print g
    h = []
    h = sorted(g)
    f = []
    #sorted numbers, apply to sort names
    for a in range(0,len(h)):
        for b in range(0,len(g)):
            if h[a] == g[b]:
                f.append(group[b])

    print group
                
    return f

print SortingFun(["Eva", "Tom", "Maja"])
