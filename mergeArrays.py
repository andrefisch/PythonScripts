def mergeArrays (f, s):
    ret = []
    while (len (f) > 0 and len (s) > 0):
        if (f[0] <= s[0]):
            ret.append(f[0])
            del f[0]
        else:
            ret.append(s[0])
            del s[0]
    if (len (f) == 0):
        ret.append(s[0])
    else:
        ret.append(f[0])
    return ret

print mergeArrays([1, 3, 5, 8], [1, 6, 7, 10])
