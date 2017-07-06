class Piece:
    def __init__(self, avatar):
        # Has the piece moved yet?
        # Relevant only in special situations
        self._hasMoved = False
        # What the piece looks like
        self._avatar = avatar
        info = list(avatar)
        # Set the color and piece type from the avatar
        self._color = info[0]
        self._type = info[1]

class Chess_Game:
    def __init__(self, turns):
        # Whose turn is it?
        # White always starts first
        self._turns = turns
        self._turn = "w"
        self._other = "b"
        self._inProgress = True
        # Board stuff
        self._w = 8
        self._h = 8
        self.set_up_board()

    # Print the board to the command line
    def print_board(self):
        DEPRINTBOARD = False
        boardString = "\n     A  B  C  D  E  F  G  H\n"
        for i in range (self._w):
            boardString += "\n"
            if i == 0:
                boardString += " 8  "
            elif i == 1:
                boardString += " 7  "
            elif i == 2:
                boardString += " 6  "
            elif i == 3:
                boardString += " 5  "
            elif i == 4:
                boardString += " 4  "
            elif i == 5:
                boardString += " 3  "
            elif i == 6:
                boardString += " 2  "
            elif i == 7:
                boardString += " 1  "
            for j in range (self._h):
                boardString += self._board[i][j]._avatar
            if i == 0:
                boardString += " 8  "
            elif i == 1:
                boardString += " 7  "
            elif i == 2:
                boardString += " 6  "
            elif i == 3:
                boardString += " 5  "
            elif i == 4:
                boardString += " 4  "
            elif i == 5:
                boardString += " 3  "
            elif i == 6:
                boardString += " 2  "
            elif i == 7:
                boardString += " 1  "
        boardString += "\n\n     A  B  C  D  E  F  G  H\n"
        return boardString  

    # Place starting pieces in correct positions
    def set_up_board(self):
        DESETUPBOARD = False
        # Make sure the board has the correct dimensions and is filled with blank pieces
        self._board = [[Piece('-- ') for x in range(self._w)] for y in range(self._h)] 
        # Set up the pawns
        for i in range (self._w):
            self._board[6][i] = Piece('wp ')
        for i in range (self._w):
            self._board[1][i] = Piece('bp ')
        # White pieces
        self._board[7][0] = Piece('wr ')
        self._board[7][7] = Piece('wr ')
        self._board[7][1] = Piece('wk ')
        self._board[7][6] = Piece('wk ')
        self._board[7][2] = Piece('wb ')
        self._board[7][5] = Piece('wb ')
        self._board[7][3] = Piece('wQ ')
        self._board[7][4] = Piece('wK ')
        # Black pieces
        self._board[0][0] = Piece('br ')
        self._board[0][7] = Piece('br ')
        self._board[0][1] = Piece('bk ')
        self._board[0][6] = Piece('bk ')
        self._board[0][2] = Piece('bb ')
        self._board[0][5] = Piece('bb ')
        self._board[0][3] = Piece('bQ ')
        self._board[0][4] = Piece('bK ')
    
    # Convert's the A-H 1-8 coordinates to board position
    def c_to_b(self, coordinate):
        DECTOB = False
        coordinates = list(coordinate.lower())
        output = ["", ""]
        letters = "abcdefgh"
        numbers = "12345678"
        if (coordinates[0] not in letters or coordinates[1] not in numbers):
            return False
        else:
            # Convert the letter coordinate to correct board position
            if (coordinates[0] == 'a'):
                output[1] = 0
            elif (coordinates[0] == 'b'):
                output[1] = 1
            elif (coordinates[0] == 'c'):
                output[1] = 2
            elif (coordinates[0] == 'd'):
                output[1] = 3
            elif (coordinates[0] == 'e'):
                output[1] = 4
            elif (coordinates[0] == 'f'):
                output[1] = 5
            elif (coordinates[0] == 'g'):
                output[1] = 6
            elif (coordinates[0] == 'h'):
                output[1] = 7
            # Convert the number coordinate to correct board position
            if (coordinates[1] == '1'):
                output[0] = 7
            elif (coordinates[1] == '2'):
                output[0] = 6
            elif (coordinates[1] == '3'):
                output[0] = 5
            elif (coordinates[1] == '4'):
                output[0] = 4
            elif (coordinates[1] == '5'):
                output[0] = 3
            elif (coordinates[1] == '6'):
                output[0] = 2
            elif (coordinates[1] == '7'):
                output[0] = 1
            elif (coordinates[1] == '8'):
                output[0] = 0
        return output
    def TEST_c_to_b(self, exIn, exOut, testNo):
        if chess.c_to_b(exIn) != exOut:
            print("c_to_b test #" + str(testNo) + " FAILED")

    # Give the turn to the nonactive player
    def toggle_turn(self):
        DETOGGLETURN = False
        if self._turn == "w":
            if DETOGGLETURN:
                print ("Now it is BLACK's turn")
            self._turn = "b"
            self._other = "w"
        else:
            if DETOGGLETURN:
                print ("Now it is WHITE's turn")
            self._turn = "w"
            self._other = "b"

    # If the move is legal move the piece at beforeCoordinate to afterCoordinate
    def make_move(self, beforeCoordinate, afterCoordinate):
        DEMAKEMOVE = False
        before = self.c_to_b(beforeCoordinate)
        after  = self.c_to_b(afterCoordinate)
        # If the move is valid
        if (before == False or after == False):
            return False
        else:
            if (self.check_move(before, after)):
                if DEMAKEMOVE:
                    print("The move from " + str(beforeCoordinate) + " to " + str(afterCoordinate) + " has been approved")
                # Move the piece
                if (self._board[after[0]][after[1]]._type == 'K'):
                    self._inProgress = False
                else:
                    self._board[after[0]][after[1]] = self._board[before[0]][before[1]]
                    # Set the old space to empty
                    self._board[before[0]][before[1]] = Piece('-- ')
                    # Record that the piece has moved
                    self._board[after[0]][after[1]]._hasMoved = True
                    # Give the turn to the nonactive player
                    if (self._turns):
                        self.toggle_turn()
                return True
            else:
                if DEMAKEMOVE:
                    print("The move from " + str(beforeCoordinate) + " to " + str(afterCoordinate) + " has NOT been approved")
                return False
    def TEST_make_move(self, before, after, testNo):
        chess.make_move(before, after)
        pos0 = chess.c_to_b(before)
        pos1 = chess.c_to_b(after)
        piece = self._board[pos0[0]][pos0[1]]._avatar
        if (self._board[pos1[0]][pos1[1]]._avatar != piece and self._board[pos0[0]][pos0[1]]._avatar != '-- '):
            print ("make_move test #" + str(testNo) + " FAILED")

    # Is moving the piece at before to after legal?
    def check_move(self, before, after):
        DECHECKMOVE = False
        if DECHECKMOVE:
            print("Now checking the move")
        # What is in the before space?
        # - It can only be a piece of the active player
        # - Must be color of current player
        # What is in the after space?
        # - It can either be a piece of the nonactive player or empty piece
        # Before space must be active player and after space must not be active player
        legalMove = False
        if (self._board[before[0]][before[1]]._color == self._turn or not self._turns):
            if (self._board[after[0]][after[1]]._color != self._turn):
                # It is the current player's piece moving to either take the opponents piece or moving to an empty space but can the piece do that?
                # If it is a pawn
                if (self._board[before[0]][before[1]]._type == 'p'):
                    legalMove = self.pawn_rules(before, after)
                # If it is a rook
                elif (self._board[before[0]][before[1]]._type == 'r'):
                    legalMove = self.rook_rules(before, after)
                # If it is a knight
                # DONE
                elif (self._board[before[0]][before[1]]._type == 'k'):
                    legalMove = self.knight_rules(before, after)
                # If it is a bishop
                elif (self._board[before[0]][before[1]]._type == 'b'):
                    legalMove = self.bishop_rules(before, after)
                # If it is a queen
                elif (self._board[before[0]][before[1]]._type == 'Q'):
                    legalMove = self.queen_rules(before, after)
                # If it is the king
                # DONE
                elif (self._board[before[0]][before[1]]._type == 'K'):
                    legalMove = self.king_rules(before, after)
        return legalMove
    
    # Is the player whose turn it is in check?
    def in_check(self, before, after):
        inCheck = False
        return inCheck

    # Can the pawn legally move from before to after?
    def pawn_rules(self, before, after):
        DEPAWNRULES = False
        if DEPAWNRULES:
            print ("now moving a pawn")
        vert  = abs(before[0] - after[0])
        horiz = abs(before[1] - after[1])
        # Pawn rules:
        # - Pawn moves one space forward unless
        #   - it is in it's starting position, then it can move 2 spaces
        #   - it is taking a piece, then it must move one space diagonally
        # - Forward depends on what color the piece is
        # - When it gets to the end it turns into a different piece
        # The move is possibly legal if the vertical distance is 1 or 2 and the horizontal distance is 0 or 1
        if ((vert == 1 or vert == 2) and horiz < 2):
            # If the pawn is white it must move north
            if (self._board[before[0]][before[1]]._color == "w" and before[0] - after[0] > 0):
                if DEPAWNRULES:
                    print("This pawn is white and is north-bound")
                # If we are going straight up the space above must be empty
                if (horiz == 0):
                    if (vert == 1 and self._board[after[0]][after[1]]._color == "-"):
                        return True
                    if (vert == 2 and self._board[before[0]][before[1]]._hasMoved == False and self._board[before[0] - 1][after[1]]._color == "-" and self._board[after[0]][after[1]]._color == "-"):
                        return True
                if (horiz == 1):
                    if (vert == 1 and horiz == 1 and self._board[after[0]][after[1]]._color == "b"):
                        return True
            # If it is black it must move south
            elif(self._board[before[0]][before[1]]._color == "b" and before[0] - after[0] < 0):
                if DEPAWNRULES:
                    print("This pawn is black and is south-bound")
                # If we are going straight down the space below must be empty
                if (horiz == 0):
                    if (vert == 1 and self._board[after[0]][after[1]]._color == "-"):
                        return True
                    if (vert == 2 and self._board[before[0]][before[1]]._hasMoved == False and self._board[before[0] + 1][after[1]]._color == "-" and self._board[after[0]][after[1]]._color == "-"):
                        return True
                if (horiz == 1):
                    if (vert == 1 and horiz == 1 and self._board[after[0]][after[1]]._color == "w"):
                        return True
        return False

    # Can the rook legally move from before to after?
    # DONE
    def rook_rules(self, before, after):
        DEROOKRULES = False
        if DEROOKRULES:
            print ("now moving a rook")
        # Rook rules:
        # - Rook moves any number of spaces horizontally or vertically
        #   - Cannot move through pieces
        vert  = abs(before[0] - after[0])
        horiz = abs(before[1] - after[1])
        if DEROOKRULES:
            print("moving from " + str(before) + " to " + str(after))
        # Check that we are moving either horizontally or vertically only
        if ((vert != 0 and horiz == 0) or (vert == 0 and horiz != 0)):
            # Which way are we going?
            # If we encounter a non-blank piece in the way the move is not legal
            # UP
            if (before[0] - after[0] > 0):
                if DEROOKRULES:
                    print ("if condition 1")
                for i in range (before[0] - 1, after[0], -1):
                    if DEROOKRULES:
                        print ("Now checking coordinate " + str(i) + ", " + str(before[1]))
                    if (self._board[i][before[1]]._avatar != "-- "):
                        if DEROOKRULES:
                            print ("bumped into something at coordinates " + str(i) + ", " + str(before[1]))
                        return False
            # DOWN
            elif (before[0] - after[0] < 0):
                if DEROOKRULES:
                    print ("if condition 2")
                for i in range (before[0] + 1, after[0]):
                    if DEROOKRULES:
                        print ("Now checking coordinate " + str(i) + ", " + str(before[1]))
                    if (self._board[i][before[1]]._avatar != "-- "):
                        if DEROOKRULES:
                            print ("bumped into something at coordinates " + str(i) + ", " + str(before[1]))
                        return False
            # LEFT
            elif (before[1] - after[1] > 0):
                if DEROOKRULES:
                    print ("if condition 3")
                for i in range (before[1] - 1, after[1], -1):
                    if DEROOKRULES:
                        print ("Now checking coordinate " + str(before[0]) + ", " + str(i))
                    if (self._board[before[0]][i]._avatar != "-- "):
                        if DEROOKRULES:
                            print ("bumped into something at coordinates " + str(before[0]) + ", " + str(i))
                        return False
            # RIGHT
            elif (before[1] - after[1] < 0):
                if DEROOKRULES:
                    print ("if condition 4")
                for i in range (before[1] + 1, after[1]):
                    if DEROOKRULES:
                        print ("Now checking coordinate " + str(before[0]) + ", " + str(i))
                    if (self._board[before[0]][i]._avatar != "-- "):
                        if DEROOKRULES:
                            print ("bumped into something at coordinates " + str(before[0]) + ", " + str(i))
                        return False
            return True
        return False
    def TEST_rook_rules(self, before, after, expected, testNo):
        if (self.rook_rules(before, after) == expected):
            pass
        else:
            print("rook movement test #" + str(testNo) + " FAILED")

    # Can the knight legally move from before to after?
    # NO KNOWN BUGS
    def knight_rules(self, before, after):
        DEKNIGHTRULES = False
        if DEKNIGHTRULES:
            print ("now moving a knight")
        # Knight rules:
        # - Knight moves two spaces in one direction and one direction in another
        #   - Knight can jump over other pieces
        vert  = abs(before[0] - after[0])
        horiz = abs(before[1] - after[1])
        # Check that we are moving exactly one space vertically and exactly two spaces horizontally or vice versa
        if ((vert == 1 and horiz == 2) or (vert == 2 and horiz == 1)):
            return True
        return False
    def TEST_knight_rules(self, before, after, expected, testNo):
        if (self.knight_rules(before, after) == expected):
            pass
        else:
            print("knight movement test #" + str(testNo) + " FAILED")

    # Can the bishop legally move from before to after?
    def bishop_rules(self, before, after):
        DEBISHOPRULES = False
        if DEBISHOPRULES:
            print ("now moving a bishop")
        # Bishop rules:
        # - Bishop moves any number of spaces diagonally
        #   - Cannot move through pieces
        vert  = abs(before[0] - after[0])
        horiz = abs(before[1] - after[1])
        # Check that we have moved the same space vertically that we have horizontally
        if (vert > 0 and vert == horiz):
            # Which way are we going?
            # If we encounter a non-blank piece in the way the move is not legal
            # UP RIGHT
            # NO KNOWN BUGS
            if (before[0] - after[0] > 0 and before[1] - after[1] < 0):
                if DEBISHOPRULES:
                    print ("if condition 1")
                for i in range (1, before[0] - after[0]):
                    if DEBISHOPRULES:
                        print ("Now checking coordinate " + str(before[0] - i) + ", " + str(before[1] + i))
                    if (self._board[before[0] - i][before[1] + i]._avatar != "-- "):
                        if DEBISHOPRULES:
                            print ("bumped into something at coordinates " + str(before[0] - i) + ", " + str(before[1] + i))
                        return False
            # DOWN RIGHT
            elif (before[0] - after[0] < 0 and before[1] - after[1] < 0):
                if DEBISHOPRULES:
                    print ("if condition 2")
                for i in range (1, after[0] - before[0]):
                    if DEBISHOPRULES:
                        print ("Now checking coordinate " + str(before[0] + i) + ", " + str(before[1] + i))
                    if (self._board[before[0] + i][before[1] + i]._avatar != "-- "):
                        if DEBISHOPRULES:
                            print ("bumped into something at coordinates " + str(before[0] + i) + ", " + str(before[1] + i))
                        return False
            # DOWN LEFT
            elif (before[0] - after[0] < 0 and before[1] - after[1] > 0):
                if DEBISHOPRULES:
                    print ("if condition 3")
                for i in range (1, after[0] - before[0]):
                    if DEBISHOPRULES:
                        print ("Now checking coordinate " + str(before[0] + i) + ", " + str(before[1] - i))
                    if (self._board[before[0] + i][before[1] - i]._avatar != "-- "):
                        if DEBISHOPRULES:
                            print ("bumped into something at coordinates " + str(before[0] + i) + ", " + str(before[1] - i))
                        return False
            # UP LEFT
            # NO KNOWN BUGS
            elif (before[0] - after[0] > 0 and before[1] - after[1] > 0):
                if DEBISHOPRULES:
                    print ("if condition 4")
                for i in range (1, before[0] - after[0]):
                    if DEBISHOPRULES:
                        print ("Now checking coordinate " + str(before[0] - i) + ", " + str(before[1] - i))
                    if (self._board[before[0] - i][before[1] - i]._avatar != "-- "):
                        if DEBISHOPRULES:
                            print ("bumped into something at coordinates " + str(before[0] - i) + ", " + str(before[1] - i))
                        return False
            return True
        return False
    def TEST_bishop_rules(self, before, after, expected, testNo):
        if (self.bishop_rules(before, after) == expected):
            pass
        else:
            print("bishop movement test #" + str(testNo) + " FAILED")

    # Can the queen legally move from before to after?
    def queen_rules(self, before, after):
        DEQUEENRULES = False
        if DEQUEENRULES:
            print ("now moving a queen")
        # Queen rules:
        # - Queen moves horizontally, vertically, or diagonally any number of spaces
        #   - Cannot move through pieces
        vert  = abs(before[0] - after[0])
        horiz = abs(before[1] - after[1])
        # Check that we are either only moving vertically or only moving horizontally or moving the same number of spaces vertically as we have horizontally
        if ((vert != 0 and horiz == 0) or (vert == 0 and horiz != 0) or (vert > 0 and vert == horiz)):
            # Which way are we going?
            # If we encounter a non-blank piece in the way the move is not legal
            # UP
            if (before[0] - after[0] > 0 and before[1] == after[1]):
                if DEQUEENRULES:
                    print ("if condition 1")
                for i in range (before[0] - 1, after[0], -1):
                    if DEQUEENRULES:
                        print ("Now checking coordinate " + str(i) + ", " + str(before[1]))
                    if (self._board[i][before[1]]._avatar != "-- "):
                        if DEQUEENRULES:
                            print ("bumped into something at coordinates " + str(i) + ", " + str(before[1]))
                        return False
            # DOWN
            elif (before[0] - after[0] < 0 and before[1] == after[1]):
                if DEQUEENRULES:
                    print ("if condition 2")
                for i in range (before[0] + 1, after[0]):
                    if DEQUEENRULES:
                        print ("Now checking coordinate " + str(i) + ", " + str(before[1]))
                    if (self._board[i][before[1]]._avatar != "-- "):
                        if DEQUEENRULES:
                            print ("bumped into something at coordinates " + str(i) + ", " + str(before[1]))
                        return False
            # LEFT
            elif (before[1] - after[1] > 0 and before[0] == after[0]):
                if DEQUEENRULES:
                    print ("if condition 3")
                for i in range (before[1] - 1, after[1], -1):
                    if DEQUEENRULES:
                        print ("Now checking coordinate " + str(before[0]) + ", " + str(i))
                    if (self._board[before[0]][i]._avatar != "-- "):
                        if DEQUEENRULES:
                            print ("bumped into something at coordinates " + str(before[0]) + ", " + str(i))
                        return False
            # RIGHT
            elif (before[1] - after[1] < 0 and before[0] == after[0]):
                if DEQUEENRULES:
                    print ("if condition 4")
                for i in range (before[1] + 1, after[1]):
                    if DEQUEENRULES:
                        print ("Now checking coordinate " + str(before[0]) + ", " + str(i))
                    if (self._board[before[0]][i]._avatar != "-- "):
                        if DEQUEENRULES:
                            print ("bumped into something at coordinates " + str(before[0]) + ", " + str(i))
                        return False
            # Which way are we going?
            # If we encounter a non-blank piece in the way the move is not legal
            # UP RIGHT
            # NO KNOWN BUGS
            if (before[0] - after[0] > 0 and before[1] - after[1] < 0):
                if DEQUEENRULES:
                    print ("if condition 5")
                for i in range (1, before[0] - after[0]):
                    if DEQUEENRULES:
                        print ("Now checking coordinate " + str(before[0] - i) + ", " + str(before[1] + i))
                    if (self._board[before[0] - i][before[1] + i]._avatar != "-- "):
                        if DEQUEENRULES:
                            print ("bumped into something at coordinates " + str(before[0] - i) + ", " + str(before[1] + i))
                        return False
            # DOWN RIGHT
            elif (before[0] - after[0] < 0 and before[1] - after[1] < 0):
                if DEQUEENRULES:
                    print ("if condition 6")
                for i in range (1, after[0] - before[0]):
                    if DEQUEENRULES:
                        print ("Now checking coordinate " + str(before[0] + i) + ", " + str(before[1] + i))
                    if (self._board[before[0] + i][before[1] + i]._avatar != "-- "):
                        if DEQUEENRULES:
                            print ("bumped into something at coordinates " + str(before[0] + i) + ", " + str(before[1] + i))
                        return False
            # DOWN LEFT
            elif (before[0] - after[0] < 0 and before[1] - after[1] > 0):
                if DEQUEENRULES:
                    print ("if condition 7")
                for i in range (1, after[0] - before[0]):
                    if DEQUEENRULES:
                        print ("Now checking coordinate " + str(before[0] + i) + ", " + str(before[1] - i))
                    if (self._board[before[0] + i][before[1] - i]._avatar != "-- "):
                        if DEQUEENRULES:
                            print ("bumped into something at coordinates " + str(before[0] + i) + ", " + str(before[1] - i))
                        return False
            # UP LEFT
            # NO KNOWN BUGS
            elif (before[0] - after[0] > 0 and before[1] - after[1] > 0):
                if DEQUEENRULES:
                    print ("if condition 8")
                for i in range (1, before[0] - after[0]):
                    if DEQUEENRULES:
                        print ("Now checking coordinate " + str(before[0] - i) + ", " + str(before[1] - i))
                    if (self._board[before[0] - i][before[1] - i]._avatar != "-- "):
                        if DEQUEENRULES:
                            print ("bumped into something at coordinates " + str(before[0] - i) + ", " + str(before[1] - i))
                        return False
            return True
        return False
    def TEST_queen_rules(self, before, after, expected, testNo):
        if (self.queen_rules(before, after) == expected):
            pass
        else:
            print("queen movement test #" + str(testNo) + " FAILED")

    # Can the king legally move from before to after?
    # NO KNOWN BUGS
    def king_rules(self, before, after):
        DEKINGRULES = False
        if DEKINGRULES:
            print ("now moving the king")
        # King rules:
        # - King moves exactly one space in any direction
        # - If the king is taken, player with lost king loses
        vert  = abs(before[0] - after[0])
        horiz = abs(before[1] - after[1])
        if ((vert == 1 and horiz == 0) or (vert == 0 and horiz == 1) or (vert == 1 and horiz == 1)):
            return True
        return False
    def TEST_king_rules(self, before, after, expected, testNo):
        if (self.king_rules(before, after) == expected):
            pass
        else:
            print("king movement test #" + str(testNo) + " FAILED")

class Play_Chess:
    def __init__(self):
        self._game = Chess_Game(True)

    def play_chess(self):
        while(self._game._inProgress):
            if (self._game._turn == "w"):
                print("\nIt is WHITE's turn to move:")
                print(self._game.print_board())
                print("What is your move, WHITE?: ")
                try:
                    before = input("Move piece at coordinates: ")
                except:
                    before = None
                try:
                    after  = input("to coordinates:            ")
                except:
                    after  = None
                if (before is None or after is None or len(before) < 2 or len(after) < 2):
                    if (before.lower() == "q" or before.lower() == "x" or after.lower() == "q" or after.lower() == "x"):
                        break
                    before, after = "--", "--"
                if (self._game.make_move(before, after)):
                    pass
                else:
                    print("Specified move is invalid, choose another move.")
            else:
                print("\nIt is BLACK's turn to move:")
                print(self._game.print_board())
                print("What is your move, BLACK?: ")
                try:
                    before = input("Move piece at coordinates: ")
                except:
                    before = None
                try:
                    after  = input("to coordinates:            ")
                except:
                    after  = None
                if (before is None or after is None or len(before) < 2 or len(after) < 2):
                    if (before.lower() == "q" or before.lower() == "x" or after.lower() == "q" or after.lower() == "x"):
                        break
                    before, after = "--", "--"
                if (self._game.make_move(before, after)):
                    pass
                else:
                    print("Specified move is invalid, choose another move.")
        if (self._game._turn == "w"):
            print("\nCONGRATULATIONS ON YOUR VICTORY, WHITE!")
        elif (self._game._turn == "b"):
            print("\nCONGRATULATIONS ON YOUR VICTORY, BLACK!")
        self._game.print_board()

game = Play_Chess()
game.play_chess()




'''
chess = Chess_Game(False)
print(chess.print_board())

# TESTS
# Test valid coordinates:
chess.TEST_c_to_b('a1', [7, 0], 1)
chess.TEST_c_to_b('h8', [0, 7], 2)
chess.TEST_c_to_b('z1', False, 3)
chess.TEST_c_to_b('a9', False, 4)

# Test make move:
# Move white pawn
# chess.make_move('b1', 'c3')
chess.TEST_make_move('d2', 'd4', 2)
chess.TEST_make_move('e2', 'e3', 3)
# chess.TEST_make_move('d1', 'h5', 9)
chess.TEST_make_move('h7', 'h5', 10)
chess.TEST_make_move('h5', 'h4', 11)
chess.TEST_make_move('h4', 'h3', 11)
chess.TEST_make_move('h2', 'h3', 5)
chess.TEST_make_move('g2', 'h3', 5)
# chess.TEST_make_move('f3', 'g3', 10)
# chess.TEST_make_move('g3', 'f5', 10)
# chess.TEST_make_move('a1', 'b1', 6)
# Move black knight
# chess.make_move('g8', 'h6')

# Test if a rook can legally move from before to after
chess.TEST_rook_rules([2, 2], [2, 7], True, 1)
chess.TEST_rook_rules([2, 2], [2, 2], False, 2)
chess.TEST_rook_rules([7, 2], [2, 7], False, 3)
chess.TEST_rook_rules([7, 7], [2, 7], True, 4)

# Test if a knight can legally move from before to after
chess.TEST_knight_rules([2, 2], [2, 7], False, 1)
chess.TEST_knight_rules([2, 2], [3, 4], True, 2)
chess.TEST_knight_rules([2, 2], [0, 1], True, 3)
chess.TEST_knight_rules([2, 2], [2, 2], False, 4)

# Test if a bishop can legally move from before to after
chess.TEST_bishop_rules([2, 2], [3, 3], True, 1)
chess.TEST_bishop_rules([2, 2], [0, 0], True, 2)
chess.TEST_bishop_rules([2, 2], [0, 1], False, 3)
chess.TEST_bishop_rules([2, 2], [2, 2], False, 4)

# Test if a queen can legally move from before to after
chess.TEST_queen_rules([2, 2], [3, 3], True, 1)
chess.TEST_queen_rules([2, 2], [7, 2], True, 2)
chess.TEST_queen_rules([2, 2], [0, 1], False, 3)
chess.TEST_queen_rules([2, 2], [2, 2], False, 4)
chess.TEST_queen_rules([2, 2], [0, 0], True, 5)
chess.TEST_queen_rules([2, 2], [2, 0], True, 6)

# Test if a king can legally move from before to after
chess.TEST_king_rules([2, 2], [3, 3], True, 1)
chess.TEST_king_rules([2, 2], [7, 2], False, 2)
chess.TEST_king_rules([2, 2], [0, 1], False, 3)
chess.TEST_king_rules([2, 2], [2, 2], False, 4)
chess.TEST_king_rules([2, 2], [2, 1], True, 5)
'''

# print(chess.print_board())
