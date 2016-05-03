def main():
    print "enter values to be analyzed, use -1 to end list"
    data = []

    num = input("enter your number: ")
    while num != -1:
        data.append(num)
        num = input("enter your number: ")
    
    avg = average(data)
    print 'average of data values is ', avg

def average(data):
    # compute average of a list of numbers
    sum = 0.0
    i = 0
    while i < len(data):
        sum = sum + data[i]
        i = i + 1
    if len (data) == 0: return 0
    else: return sum / len(data)

main()
