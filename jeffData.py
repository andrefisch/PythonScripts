import math
DEBUG = True

# how different can you be while still being the same, how similar can you be while still being different?
# pass an array of tuples, where the first value of each tuple is the group, second is x coordinate and third is y coordinate
# should return an array of tuples where the 
# - first value of each tuple is how different can you be while still being the same
# - second value of each tuple is how similar can you be while still being different
def calcDiff(arr):
    output = {}
    # how many species do we have
    species = []
    for i in range (0, len(arr)):
        if arr[i][0] not in species:
            species.append(arr[i][0])
            output[arr[i][0]] = [0, -1]
    if DEBUG:
        # check to make sure we have the correct number of output arrays
        print "Length of output is", len(output)
    for i in range (0, len(arr)):
        for j in range (i, len(arr)):
            if DEBUG:
                print "i =", i, "j =", j
            # loop through and test each point against each other point
            temp = distance(arr[i], arr[j])
            # if two species are the same, save the data if it is greater than greatest recorded data for that species
            if arr[i][0] == arr[j][0]:
                if temp > output[arr[i][0]][0]:
                    output[arr[i][0]][0] = temp
            # otherwise they are different so record the value in both of the correct places if applicable
            else:
                if temp < output[arr[i][0]][1] or output[arr[i][0]][1] < 0:
                    output[arr[i][0]][1] = temp
                if temp < output[arr[j][0]][1] or output[arr[j][0]][1] < 0:
                    output[arr[j][0]][1] = temp
    return output 

# take two tuples from the data in calcDiff arr from above and find the distance between them
def distance(d0, d1):
    return math.sqrt((d0[1] - d1[1]) ** 2 + (d0[2] - d1[2]) ** 2)

if DEBUG:
    # answer for this array should be:
    # {Gbberingei: [1.0, 1.0], Gbgrauri: [2.0, 2.0], Gggorilla: [9.0, 1.0]}
    primateArray = [("Gbberingei", 0, 1), ("Gbberingei", 0, 2), ("Gbgrauri", 0, 4), ("Gbgrauri", 0, 6), ("Gggorilla", 0, 9), ("Gggorilla", 0, 0)]
    print "Length of primate test array is", len(primateArray)
    print distance (primateArray[0], primateArray[1])
    print calcDiff(primateArray)
