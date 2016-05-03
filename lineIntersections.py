def lineIntersections(n, s, e):
    p = 0
    # go through all numbers in the first array except the last one
    for i in range (n - 1):
        # check through all numbers in the second array that are greater than position we are at in the first
        for j in range (i + 1, n):
            # print "Now checking", i, "and", j
            if s[i] <= s[j] <= e[i] or s[j] <= s[i] <= e[j]:
                p += 1
                print "the pair that overlaps is", i, "and", j
    return p

print lineIntersections(4, [8, 4, 6, 1], [10, 9, 7, 2]), "INTERSECTIONS"
print "2 EXPECTED"
print lineIntersections(3, [1, 3, 5], [2, 4, 6]), "INTERSECTIONS"
print "0 EXPECTED"
print lineIntersections(2, [1, 2], [3, 4]), "INTERSECTIONS"
print "1 EXPECTED"
print lineIntersections(1, [1], [2]), "INTERSECTIONS"
print "0 EXPECTED"
print lineIntersections(2, [1, 3], [3, 8]), "INTERSECTIONS"
print "1 EXPECTED"
print lineIntersections(3, [1, 1, 1], [2, 2, 2]), "INTERSECTIONS"
print "3 EXPECTED"
