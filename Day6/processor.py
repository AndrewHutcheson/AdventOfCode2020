stream = open("input.txt")
lines = stream.readlines()

#part1
groups = dict()
n = 0
total = 0

for line in lines:
    if (line != "\n"):
        if(n in groups.keys()):
            groups[n] = groups[n] + line.strip("\n")
        else:
            groups[n] = line.strip("\n")
    else:
        numChars = len(set(groups[n]))
        total = total + numChars
        n = n + 1
    #need to check lasy line since not \n
    if(line is lines[-1]):        
        numChars = len(set(groups[n]))
        total = total + numChars
        n = n + 1

print(total)

#part 2
groupQuestions = set()
tempGroupQuestions = groupQuestions.copy()
groups = dict()
n = 0
total = 0

for line in lines:
    if (line != "\n"):
        if(n in groups.keys()):
            groups[n] = groups[n] + line.strip("\n")
            for c in groupQuestions:
                if(c not in line.strip("\n")):
                    tempGroupQuestions.remove(c)
            groupQuestions = tempGroupQuestions.copy()
        else:
            groups[n] = line.strip("\n")
            groupQuestions = set(line.strip("\n"))
            tempGroupQuestions = groupQuestions.copy()
    else:
        numChars = len(set(groupQuestions))
        total = total + numChars
        n = n + 1
        groupQuestions = set()
    #need to check lasy line since not \n
    if(line is lines[-1]):        
        numChars = len(set(groupQuestions))
        total = total + numChars
        n = n + 1

print(total)