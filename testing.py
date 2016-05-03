import re

def compress(s):
    r = re.sub(r"(.)\1+", r"\1", s)
    return r

print compress("zz000!!G")
