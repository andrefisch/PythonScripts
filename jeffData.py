import math
DEBUG = False

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
    num = 0
    length = 0
    # { this can be removed but it ensures that the program will not throw an error if a data point has less dimensions than another datapoint
    if len(d0) <= len(d1):
        length = len(d0)
    else:
        length = len(d1)
    # }
    # distance formula for N dimensions where N is an unknown number
    for i in range (1, len(d0)):
        # distance formula in N + 1 steps: loop through N dimensions aggregating the squares of the differences
        num += (d0[i] - d1[i]) ** 2
    # then sqrt it all at once at the end
    return math.sqrt(num)

if DEBUG:
    # answer for this array should be:
    # {Gbberingei: [1.0, 1.0], Gbgrauri: [2.0, 2.0], Gggorilla: [9.0, 1.0]}
    primateArray = [("Gbberingei", 0, 1, 0), ("Gbberingei", 0, 2, 0), ("Gbgrauri", 0, 4, 0), ("Gbgrauri", 0, 6, 0), ("Gggorilla", 0, 9, 0), ("Gggorilla", 0, 0, 0)]
    print "Length of primate test array is", len(primateArray)
    print distance (primateArray[0], primateArray[1])
    print calcDiff(primateArray)

jeffData = [(2,   0.0295245621,    -0.0346388028),
(2,   -0.1592206205,   -0.1292587769),
(2,   -0.0279865484,   -0.0102584277),
(2,   0.0213329541,    -0.0590473527),
(2,   0.0186482652,    -0.0284362353),
(2,   -0.0939528258,   0.0560606904),
(2,   -0.0617759046,   -0.002480195),
(2,   -0.0221723168,   -0.1453466513),
(1,   0.0375994251,    0.0185098192),
(1,   -0.0554840269,   -0.0317779277),
(1,   0.049232825, -0.0801758889),
(1,   0.0265247108,    0.0727297007),
(1,   -0.0051707276,   0.0467700551),
(1,   -0.1505356262,   0.0023422183),
(1,   -0.2586979915,   0.0332550498),
(1,   -0.0712646751,   -0.0759150282),
(1,   -0.0669691657,   -0.0497186545),
(1,   -0.1862904045,   0.0632757285),
(1,   -0.1189739372,   -0.0578387149),
(3,   0.1621280547,    -0.0541050934),
(3,   0.2954777406,    0.116909307),
(3,   0.1178347211,    -0.0528647849),
(3,   -0.0092498713,   0.0376092302),
(3,   0.205165106, 0.1666655727),
(3,   0.1715704139,    -0.0652599082),
(3,   -0.2059674103,   0.2112276175),
(3,   -0.0772234853,   0.0841218434),
(3,   0.2485358622,    0.043009143),
(3,   0.1873608969,    -0.0753635334)]

print distance(jeffData[0], jeffData[1])
print calcDiff(jeffData)
