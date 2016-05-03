"""
This program takes a textfile as an input and prints the instances of all words
and how frequently in the document they occur.
"""

import sys

print 'Argument List:', 

def compareIndexOne (x, y):
  if x[1] < y[1]: return -1
  if x[1] == y[1]: return 0
  return 1

def frequency(lst):
    import string
    
    f = open(lst)
    flst = f.readlines()
    slst = ''.join(flst)
    lcslst = slst.lower()
    lcwpslst = lcslst.translate(string.maketrans("",""), string.punctuation)
    lcwpsslst = lcwpslst.split()
    f.close()
    
    counts = {}
    for ele in lcwpsslst:
        counts[ele] = counts.get(ele, 0) + 1

    dctlst = counts.items()
    dctlst.sort(compareIndexOne)
    
    for element in dctlst:
        print 'freq,word: ', element[1], ",", element[0]

print frequency(str(sys.argv[1]))
