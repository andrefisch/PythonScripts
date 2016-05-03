def ChessboardShapes(q):
    
    if q == []:
        return 1
    
    t = range(8)
    
    # populate board
    b = [[1 if i % 2 == j % 2 else 0 for i in t] for j in t]

    # calc count on adding each square
    m = 0
    for s in q:
        # unpack coordinate, e.g. a3
        x,y = s
        x = ord(x) - 97
        y = int(y) - 1
        
        # set square to black
        b[x][y] = 1
    
        # get count from this square
        c = a(x,y,b)
        
        m = max(m,c)
        
        # reset any values that were set to 2 (indicating that we already counted them)
        for i in t:
            for j in t:
                if b[i][j] > 0:
                    b[i][j] = 1
        
    return m

# calculate area recursively
def a(x,y,b):
    z = 0
    if 0 <= x < 8 and 0 <= y < 8 and b[x][y] == 1:
        b[x][y] = 2
        z = 1 + a(x+1,y,b) + a(x - 1,y,b) + a(x,y + 1,b) + a(x,y - 1,b)
    return z
