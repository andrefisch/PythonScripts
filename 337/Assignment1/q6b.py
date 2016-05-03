lowNum = input("Choose a low number greater than 2: ")
highNum = input("Choose a high number: ")

primes = []

# checks all numbers in the specified range with the Python statement given to
# us in 6a. if the list that statement creates is empty it means that the number
# has no multiples, which means that it is prime so it gets added to the prime
# list
currNum = lowNum
while currNum < highNum:
    if len([x for x in range(2, currNum) if currNum % x == 0]) == 0:
        primes.append(currNum)
    currNum += 1

print primes
