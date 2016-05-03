ff = raw_input("Enter a file name: ")
f = open(ff)

flst = f.readlines()

count = 0
info = ""

# records information in string form about files without . extensions at the end
while count < len(flst):
    tmp = flst[count].split()
    if tmp[0] >= 30 and tmp[3].count(".") == 0:
        info += "".join(flst[count])
    count += 1

# number of files
size = len(flst)
slst = ' '.join(flst)

# number of each type of file
python = slst.count(".py")
perl = slst.count(".pl")
javascript = slst.count(".js")
other = size - (python + perl + javascript)

print "There are a total of", size, "files, including:"
print javascript, "JavaScript files,", perl, "perl scripts,", python, "python scripts, and", other, "other files"
print "Among the", other, "other files, the following have 30 or more lines:"
print info
