# re.sub(pattern, repl, string, count=0, flags=0)
import re
s = "zz000!!G"
replaced = re.sub(r"(.)\1+", r"\1", s)
print replaced 
