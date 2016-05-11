import re
from fractions import gcd

def chemistry(f, s):
    c = re.sub(r"(\w+\(\d+\))(\w+\(\d+\))(\w+\(\d+\))(\w+\(\d+\))", r"\3\2\1\4", f + s)
    l = re.findall('\w+', c)
    d = gcd(l[1],l[3])
    l[1] = l[1] / d
    l[3] = l[3] / d
    d = gcd(l[5],l[7])
    l[5] = l[5] / d
    l[7] = l[7] / d
    return l

print chemistry("Ba(1)Cl(2)", "H(2)SO4(1)")

