listy = raw_input("Enter a list in square brackets: ")
slisty = listy[1:len(listy)-1]
sslisty = slisty.split(", ")

print "After removing 0's, the list becomes"

# removes 0's with a for loop by going through the list and if the current
# character is not a 0, add it to the output list
output = []
for x in sslisty:
    if int(x) != 0:
        output.append(int(x))

print output

# removes 0's with a while loop by going through the list and if the current
# character is not a 0, add it to the output list
count = 0
output = []
while count < len(sslisty):
    if int(sslisty[count]) != 0:
        output.append(int(sslisty[count]))
    count += 1
    
print output

# removes 0's with a for loop by going through the list and adding all elements
# but if the current element is 0 it skips this iteration
output = []
for x in sslisty:
    if int(x) == 0:
        continue
    output.append(int(x))

print output
