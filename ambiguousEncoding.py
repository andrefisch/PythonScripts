def AmbiguousEncoding(s):
    x = y = 1
    p = '0'
    for c in s:
        y *= c > '0'
        x *= '09' < p + c < '27'
        y += x
        x = y - x
        
        p = c
    
    return y % 1000003
