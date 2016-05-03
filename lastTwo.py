# lastTwo = lambda n, k: str(pow(n % 100 if n % 100 > 9 else n, k % 100))[-2:]
lastTwo = lambda n, k: ('0' + str((n % 100) ** (k % 100)))[-2:]

print lastTwo(341978, 63415)
print lastTwo(78, 15)

print lastTwo(97071, 9188)
print lastTwo(71, 88)

print lastTwo(101, 1)
