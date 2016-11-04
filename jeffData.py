import math
import sys
import re
import os

DEBUG = False
# vim marks
# This is a useless comment


# mark i: def importTextFile():
# mark c: def calcDiff(arr):
# mark d: def distance(d0, d1):
# mark p: def printIndividualResults(arr, individuals, averages):
# mark r: # RUNNING THE SCRIPT #
# mark t: # TESTING AREA #

##############
# HOW TO RUN #
##############
howToRun = '''
You must enter a file to process. To do that from command line type 

python jeffData.py apes.txt

where apes.txt is the name of your data file. I have set the script to run on text
files where the data was exported the same exact way as the data you have given
me. If the data is formatted like that the script should run easily and with
no problems.

Did you want to use one of these files?
'''


# imports the first command line argument if one was given
def importTextFile():
    data = []
    if len(sys.argv) <= 1:
        print howToRun
        os.system("ls *.txt")
        print
    else:
        f = open(sys.argv[1], 'r')
        lines = f.readlines()
        # for each line except the first put each value into an array
        # first line with column names is ignored:
        for i in range(1, len(lines)):
            # regex which splits a string by any number of spaces
            values = re.split(" +", lines[i])
            # value[1] must be a string since it is the species name otherwise all values must be floats
            for j in range(0, len(values)):
                if j != 1:
                    values[j] = float(values[j])
                if j == 0:
                    values[j] = int(values[j])
            if DEBUG:
                print values
            data.append(values)
    return data

# how different can you be while still being the same, how similar can you be while still being different?
# pass an array of tuples, where the first value of each tuple is the group, second is x coordinate and third is y coordinate
# individuals array stores distance information where the
# - first value of each array is individual value for how different can you be while still being the same
# - second value of each array is individual value for how similar can you be while still being different
# averages dictionary calculates the averages for the species where the
# - first value of each array is cumulative value of how different can you be while still being the same
# - second value of each array is cumulative value of how similar can you be while still being different
# - third value of each array is the number of individuals in the species for averaging purposes
def calcDiff(arr):
    individuals = []
    averages = {}
    species = []
    # how many species do we have
    # this is for the averages for each species
    for i in range (0, len(arr)):
        if arr[i][1] not in species:
            species.append(arr[i][1])
            # set totals to 0 and species count to 1
            averages[arr[i][1]] = [0, 0, 1]
        else:
            # we are seeing this species again so increment the species count
            averages[arr[i][1]][2] += 1
    if DEBUG:
        # check to make sure we have the correct number of averages arrays
        print "Length of averages is", len(averages)
    # populate the array with baby arrays for 
    for i in range (0, len(arr)):
        individuals.append([0, -1])
    for i in range (0, len(arr)):
        for j in range (i, len(arr)):
            # loop through and test each point against each other point
            temp = distance(arr[i], arr[j])
            if DEBUG:
                print "i =", i, "j =", j, "distance:", temp
            # if two species are the same, save the data if it is greater than greatest recorded data for that species and update the intraspecies average and distance
            if arr[i][1] == arr[j][1]:
                # update the average for the inner loop species no matter what
                averages[arr[i][1]][0] += temp
                if temp > individuals[i][0]:
                    # update the individual only if its applicable
                    individuals[i][0] = temp
                if temp > individuals[j][0]:
                    # update the individual only if its applicable
                    individuals[j][0] = temp
            # otherwise they are different so record the value in both of the correct places if applicable
            else:
                # update the average for the inner loop species no matter what
                averages[arr[i][1]][1] += temp
                # and update the interspecies distance for one or both species, whatever is applicable 
                if temp < individuals[i][1] or individuals[i][1] < 0:
                    individuals[i][1] = temp
                if temp < individuals[j][1] or individuals[j][1] < 0:
                    individuals[j][1] = temp
    if (not DEBUG):
        printIndividualResults(arr, individuals, averages)

# take two tuples from the data in calcDiff arr from above and find the distance between them
def distance(d0, d1):
    num = 0
    length = 0
    # distance formula for N dimensions where N is an unknown number
    # the first number in the range should correspond to the first dimension to be analyzed
    for i in range (2, len(d0)):
        # distance formula in N + 1 steps: loop through N dimensions aggregating the squares of the differences
        num += (d0[i] - d1[i]) ** 2
    # then sqrt it all at once at the end
    return math.sqrt(num)

def printIndividualResults(arr, individuals, averages):
    print "                Individual Distances"
    print "####    Max.Same.Species     Min.Diff.Species"
    for i in range (0, len(individuals)):
        print "%4d    %16.14f     %16.14f" % (arr[i][0], individuals[i][0], individuals[i][1])

######################
# RUNNING THE SCRIPT #
######################

data = importTextFile()
if len(data) > 0:
    calcDiff(data)

######################
######################
######################

################
# TESTING AREA #
################

if DEBUG:
    # answer for this array should be:
    # {Gbberingei: [1.0, 1.0], Gbgrauri: [2.0, 2.0], Gggorilla: [9.0, 1.0]}
    primateArray = [(0, "Gbberingei", 0, 1, 0), (1, "Gbberingei", 0, 2, 0), (2, "Gbgrauri", 0, 4, 0), (3, "Gbgrauri", 0, 6, 0), (4, "Gggorilla", 0, 9, 0), (5, "Gggorilla", 0, 0, 0)]
    print "Length of primate test array is", len(primateArray)
    print distance (primateArray[0], primateArray[1])
    print calcDiff(primateArray)

jeffData = [(1, 2,   0.0295245621,    -0.0346388028),
(2,  2,   -0.1592206205,   -0.1292587769),
(3,  2,   -0.0279865484,   -0.0102584277),
(4,  2,   0.0213329541,    -0.0590473527),
(5,  2,   0.0186482652,    -0.0284362353),
(6,  2,   -0.0939528258,   0.0560606904),
(7,  2,   -0.0617759046,   -0.002480195),
(8,  2,   -0.0221723168,   -0.1453466513),
(9,  1,   0.0375994251,    0.0185098192),
(10, 1,   -0.0554840269,   -0.0317779277),
(11, 1,   0.049232825, -0.0801758889),
(12, 1,   0.0265247108,    0.0727297007),
(13, 1,   -0.0051707276,   0.0467700551),
(14, 1,   -0.1505356262,   0.0023422183),
(15, 1,   -0.2586979915,   0.0332550498),
(16, 1,   -0.0712646751,   -0.0759150282),
(17, 1,   -0.0669691657,   -0.0497186545),
(18, 1,   -0.1862904045,   0.0632757285),
(19, 1,   -0.1189739372,   -0.0578387149),
(20, 3,   0.1621280547,    -0.0541050934),
(21, 3,   0.2954777406,    0.116909307),
(22, 3,   0.1178347211,    -0.0528647849),
(23, 3,   -0.0092498713,   0.0376092302),
(24, 3,   0.205165106, 0.1666655727),
(25, 3,   0.1715704139,    -0.0652599082),
(26, 3,   -0.2059674103,   0.2112276175),
(27, 3,   -0.0772234853,   0.0841218434),
(28, 3,   0.2485358622,    0.043009143),
(29, 3,   0.1873608969,    -0.0753635334)]

# calcDiff(jeffData)
