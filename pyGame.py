import math

# are we debugging
DEBUG = True

# constants for the game
GAMEROWS = 9
GAMECOLUMNS = 6
ARRAYROWS = 10
ARRAYCOLUMNS = 8

# variables for the game
level = 0
score = 0

# do the two blocks match?
def match(board, x1, y1, x2, y2):
    # if the blocks arent the same type no more checking needs to be done
    if board[x1][y1] == board[x2][y2]:
        # if the blocks are adjacent we are done and no more checking needs to happen
        if adjacent(board, x1, y1, x2, y2):
            board[x1][y1] == 0
            board[x2][y2] == 0
        # now the fun begins: we need to see if the two blocks can be connected by a
        # straight line that turns 90* no more than twice with no other blocks in the way
        # lets test this with 5, 1 and 8, 1.
        # METHOD:
        # - can we straight shot? if so, done. if not
        #   - check above, to left, to right, and below (if not on bottom) for adjacent 0's
        #   - if 0 exists go as many spaces as possible before stopping
        #   - check if there is a 0 at relevant new angle
        #   - if 0 exists go as many spaces as possible before stopping
        #   - check if there is a 0 at relevant new angle
        #   - if there is a straightShot from here to block 2, done and there is a match
        else: 
            # if the blocks are in the same row or column:
            # straightShot from nonadjacent block to block: easy, we are done
            if (x1 == x2 or y1 == y2):
                if straightShot(board, x1, y1, x2, y2)[0]:
                    print "derp"
            # not so easy...
            else:
                checkMatchTrails(board, createMatchTrail(board, x1, y1), createMatchTrail(board, x2, y2))
    else: 
        return board

# are the two blocks adjacent?
# works correctly
def adjacent(board, x1, y1, x2, y2):
    if (abs(x1 - x2) == 1 and abs(y1 - y2) != 1) or (abs(x1 - x2) != 1 and abs(y1 - y2) == 1):
        if DEBUG:
            print "Now comparing", board[x1][y1], "and", board[x2][y2]
        if (board[x1][y1] == board[x2][y2]):
            return True
        else:
            return False
    else:
        return False

# checks to see if there is anything but 0's between the two spots
# will even work with indeces that are one out of bounds so we can
# test blocks on the edge against each other
def straightShot(board, x1, y1, x2, y2):
    output = [False, 0]
    if (x1 == x2):
        # condition works
        if y2 > y1:
            for y in range(y1 + 1, y2):
                if board[x1][y] == 0:
                    output[1] += 1
                else:
                    return output
        # condition works
        else:
            for y in range(y2 + 1, y1):
                if board[x1][y] == 0:
                    output[1] += 1
                else:
                    return output
        output[0] = True
    elif (y1 == y2):
        # condition works
        if x2 > x1:
            for x in range(x1 + 1, x2):
                if board[x][y1] == 0:
                    output[1] += 1
                else:
                    return output
        # condition works
        else:
            for x in range(x2 + 1, x1):
                if board[x][y1] == 0:
                    output[1] += 1
                else:
                    return output
        output[0] = True
    return output

# creates a trail of -1's from all possible directions of input block
# works correctly
def createMatchTrail(board, x1, y1):
    output = []
    # create a trail in up to 4 possible directions for both blocks
    # check down only if we are not at the bottom row
    if (x1 + 1 < ARRAYROWS):
        if DEBUG:
            print "now checking down"
        for i in range (x1 + 1, ARRAYROWS):
            if DEBUG:
                print "Now checking", str(i) + "," + str(y1)
            if board[i][y1] == 0:
                board[i][y1] = -1
                output.append([i, y1])
            else:
                break
    # check up
    if DEBUG:
        print "now checking up"
    for i in range (x1 - 1, -1, -1):
        if DEBUG:
            print "Now checking", str(i) + "," + str(y1)
        if board[i][y1] == 0:
            board[i][y1] = -1
            output.append([i, y1])
        else:
            break
    # check rightdown
    if DEBUG:
        print "now checking right"
    for i in range (y1 + 1, ARRAYCOLUMNS):
        if DEBUG:
            print "Now checking", str(x1) + "," + str(i)
        if board[x1][i] == 0:
            board[x1][i] = -1
            output.append([x1, i])
        else:
            break
    # check left
    if DEBUG:
        print "now checking left"
    for i in range (y1 - 1, -1, -1):
        if DEBUG:
            print "Now checking", str(x1) + "," + str(i)
        if board[x1][i] == 0:
            board[x1][i] = -1
            output.append([x1, i])
        else:
            break
    return output

# checks to see if there is a straightShot between any -1 in list1 and list2
def checkMatchTrails(board, list1, list2):
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if straightShot(board, list1[i][0], list1[i][1], list2[j][0], list2[j][1])[0]:
                return True
    return False

# remove all -1's from the board
# works correctly
def matchTrailCleanup(board):
    for i in range (0, len(board)):
        for j in range (0, len(board[0])):
            if board[i][j] == -1:
                board[i][j] = 0

# print the board
def dislayBoard(board):
    for i in range (0, len(board)):
        print board[i]

testArray = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 3, 1, 5, 5, 4, 4, 0],
             [0, 4, 2, 2, 1, 2, 5, 0],
             [0, 1, 1, 1, 2, 5, 2, 0],
             [0, 5, 3, 1, 3, 3, 3, 0],
             [0, 4, 2, 1, 2, 1, 4, 0]]
if DEBUG:
    # print straightShot(testArray, 5, 6, 9, 6)
    # print straightShot(testArray, 5, 6, 5, ARRAYCOLUMNS)
    # print straightShot(testArray, 5, -1, 5, 1)
    # print adjacent(testArray, 4, 3, 4, 4)
    dislayBoard(testArray)
    print checkMatchTrails(testArray, createMatchTrail(testArray, 5, 1), createMatchTrail(testArray, 8, 1))
    dislayBoard(testArray)
    matchTrailCleanup(testArray)
    print
    dislayBoard(testArray)

# towards(x), towards(y), towards(x)
# towards(y), towards(x), towards(y)
# away(x), towards(y), towards(x)
# away(y), towards(x), towards(y)
