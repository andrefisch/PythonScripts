NPalindromes = lambda s: sum([p(s,i,i) + p(s,i,i+1) for i in range(len(s))])

p = lambda s,l,r: p(s, l - 1, r + 1) + [0,1][l != r] if l >= 0 and r < len(s) and s[l] == s[r] else 0


