def ChessboardShapes(squares):
    a = 1
    print "Squares ", squares

    board = [[0 for x in range(8)] for y in range(8)] 
    FillBoard(board)

    for i in squares:
        # take array info and fill in chessboard
        for j in squares:
            n, l = j
            n = ord(n) - 97
            l = int(l) - 1
            print "changing", n, ",", l, "to 1"
            board[n][l] = 1

        # then find area
        n, l = j
        n = ord(n) - 97
        l = int(l) - 1
        t = FindArea(n, l, board)
        for x in range (8):
            for y in range (8):
                print board[x][y],
                if y == 7:
                    print "\n"
        FillBoard(board)
        if t > a:
            a = t

    return a

def FindArea(n, l, board):
    s = 1
    # if we have a number in the middle of the board it is easy
    # if this part of the board is shaded we are done
    if board[n][l] == 0:
        return 0
    # if this part of the board is shaded we recurse
    else:
        # mark the square so we dont count it twice
        board[n][l] = 0
        # call the method in four directions
        if n < 7:
            print "case 1:", n, ", ", l
            s += FindArea (n + 1, l, board)
        if l < 7:
            print "case 2:", n, ", ", l
            s += FindArea (n, l + 1, board)
        if n > 0:
            print "case 3:", n, ", ", l
            s += FindArea (n - 1, l, board)
        if l > 0:
            print "case 4:", n, ", ", l
            s += FindArea (n, l - 1, board) 
        return s

def FillBoard(board):
    s = 0
    # populate chessboard
    for i in range (8):
        s += 1
        for j in range (8):
            board[i][j] = 0 if s % 2 == 0 else 1
            s += 1


# print ChessboardShapes(["g2", "h1"])
# around the edges
print ChessboardShapes(["a2", "a4", "a6", "a8", "c8", "e8", "g8", "h7", "h5", "h3", "h1", "f1", "d1", "b1"])
# all white squares
# print ChessboardShapes(["a8", "a6", "a4", "a2", "b7", "b5", "b3", "b1", "c8", "c6", "c4", "c2", "d7", "d5", "d3", "d1", "e8", "e6", "e4", "e2", "f7", "f5", "f3", "f1", "g8", "g6", "g4", "g2", "h7", "h5", "h3", "h1"])
# all black squares
# print ChessboardShapes(["a9", "a7", "a5", "a3", "b8", "b6", "b4", "b2", "c1", "c7", "c5", "c3", "d8", "d6", "d4", "d2", "e1", "e7", "e5", "e3", "f8", "f6", "f4", "f2", "g1", "g7", "g5", "g3", "h8", "h6", "h4", "h2"])
