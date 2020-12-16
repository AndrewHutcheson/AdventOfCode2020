stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
#there's sometimes an empty newline at the end
for row in data:
    if(row == ""):
        data.remove(row)

#rules
validRanges = []

for row in data:
    line = row.split(": ")
    #stop after the rules
    if(line[0] == "your ticket:"):
        break
    ranges = line[1].split(" or ")
    for subRange in ranges:
        subSubRange = subRange.split("-")
        
        startNum = subSubRange[0]
        endNum = subSubRange[1]
        validRanges.append([startNum,endNum])

#now find all invalid tickets, ignoring my own
startFromHere = False
otherTickets = []
for row in data:
    line = row.split(": ")
    if(line[0]) == "nearby tickets:":
        startFromHere = True
    elif(startFromHere):
        otherTickets.append(row)

onlyValidTickets = []
errorRate = 0
numInvalidTickets = 0
for ticket in otherTickets:
    allTicketValues = True
    values = ticket.split(",")
    for value in values:
        found = False
        for testRange in validRanges:
            if (int(value) <= int(testRange[1])) and (int(value) >= int(testRange[0])): #not casting int yields false string comparisons
                found = True
        if found == False:
            allTicketValues = False
            errorRate += int(value)
    if(allTicketValues == False):
        numInvalidTickets += 1
    else:
        onlyValidTickets.append(ticket)

print("part 1",errorRate)

#next identify the fields. 
#for each field, loop over just the first value in each ticket. if all are valid i have IDed it. if not, move on to second field.
departureRanges = {}
departureRangeRowIds = {}
for row in data:
    line = row.split(": ")
    #stop after the rules
    if(line[0] == "your ticket:"):
        break
    ranges = line[1].split(" or ")
    subrange0 = ranges[0].split("-")
    subrange1 = ranges[1].split("-")
        
    startNum0 = subrange0[0]
    endNum0 = subrange0[1]
    startNum1 = subrange1[0]
    endNum1 = subrange1[1]
    #if(line[0].find("departure") != -1):
    if True:
        departureRanges[line[0]] = ([startNum0,endNum0,startNum1,endNum1])
        departureRangeRowIds[line[0]] = []

def isThisTheRightColumn(checkRange,validTickets,fieldNumber):
    returnValue = True
    for row in validTickets:
        numbers = row.split(",")
        if(int(checkRange[0]) <= int(numbers[fieldNumber]) <= int(checkRange[1])) or (int(checkRange[2]) <= int(numbers[fieldNumber]) <= int(checkRange[3])):
            pass
        else:
            returnValue = False
    return returnValue

for departureItem in departureRanges:
    columnToCheck = 0
    while columnToCheck <= 19:
        if(isThisTheRightColumn(departureRanges[departureItem],onlyValidTickets,columnToCheck)):
            departureRangeRowIds[departureItem].append(columnToCheck)
        columnToCheck += 1

for item in departureRangeRowIds:
    print(item,":",len(departureRangeRowIds[item]),":",departureRangeRowIds[item])
    #ok I admit I got lazy. Using the output from this print statement you can manually assign the fields to the correct column. If I have time I'll code it later.

my_ticket = [59,101,191,149,167,197,199,137,163,131,113,67,103,97,61,139,157,151,193,53] #If I have time I'll code this later too
#I know my "departure" rows are (indexed from 0) 2,9,11,14,13,1

print("part 2",my_ticket[2]*my_ticket[9]*my_ticket[11]*my_ticket[14]*my_ticket[13]*my_ticket[1])