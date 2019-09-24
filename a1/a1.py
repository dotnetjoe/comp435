import fileinput

hexCount = {}

for line in fileinput.input():
    line = int(line, 16)

    if line not in hexCount:
        # If the line isn't a duplicate, initialize the number of times it has appeared
        hexCount[line] = 1
    else:
        # If the line is a duplicate, increment the amount of times it appears
        hexCount[line] += 1

intValues = list(hexCount.keys())
intValues.sort() 

for intValue in intValues:
    if hexCount[intValue] > 1:
        # print hex followed by the number of times it appears
        print("%x %d" % (intValue, hexCount[intValue])) 
