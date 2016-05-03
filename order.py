def order(a):
    # 0 is unsorted, 1 is ascending, 2 is descending
    c = ""
    l = ""
    
    # start with the 2nd element in the array
    for i in range (1, len(a)):
        if (a[i] > a[i - 1]):
            c = "ascending"
        else:
            c = "descending"
        # if this is the first iteration of the loop we set the two values to be the same
        if (i == 1):
            l = c
        if (l != c):
            l = "not sorted"
            break

    return l

print order ([10, 5, 4]), "set"
print "descending expected"
print order ([6, 20, 160, 420]), "set"
print "ascending expected"
print order ([1, 7, 0, 4, 8, 1]), "set"
print "not sorted expected"
print order ([1, 2, 3]), "set"
print "ascending expected"
print order ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), "set"
print "ascending expected"
