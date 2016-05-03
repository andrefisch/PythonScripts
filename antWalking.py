import math

def antWalking(n):
    n, d = pow(math.factorial(n) / pow(math.factorial(n / 2), 2), 2), pow(4, n)
    m = gcd(d, n)
    if (m != 0):
        return [n / m, d / m]
    else:
        return [n, d]
    
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print antWalking(2)
print antWalking(4)
print antWalking(6)
print antWalking(8)
print antWalking(10)
print antWalking(12)
print antWalking(14)
print antWalking(16)
print antWalking(18)
print antWalking(20)
print antWalking(22)
print antWalking(24)
print antWalking(26)
print antWalking(28)
print antWalking(30)
print antWalking(32)
print antWalking(34)
print antWalking(36)
print antWalking(38)
print antWalking(40)
print antWalking(42)
print antWalking(44)
print antWalking(46)
print antWalking(48)
print antWalking(50)
print antWalking(52)
print antWalking(54)
print antWalking(56)
print antWalking(58)
print antWalking(60)
print antWalking(62)
print antWalking(64)
print antWalking(66)
print antWalking(68)
print antWalking(70)
print antWalking(72)
print antWalking(74)
print antWalking(76)
print antWalking(78)
print antWalking(80)
print antWalking(82)
print antWalking(84)
print antWalking(86)
print antWalking(88)
print antWalking(90)
print antWalking(92)
print antWalking(94)
print antWalking(96)
print antWalking(98)
print antWalking(100)
