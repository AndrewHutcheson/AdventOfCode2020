stream = open("input.txt")
lines = stream.readlines()

bagDictionary = dict()

for line in lines:
    templine = line.strip(".\n")#last character on each line
    templine = templine.replace("bags","bag") #so we dont have to go through string matching issues
    parsedLine = templine.split(" contain ")
    parent = parsedLine[0]
    children = parsedLine[1].split(", ")
    bagDictionary[parent] = children

#part 2
def iterateAllBagsInBag(bag):
    counter = 0
    for subBag in bagDictionary[bag]:
        if(subBag != "no other bag"):    
            subBagName = subBag[2:len(subBag)]
            parentCount = int(subBag[0:2])
            counter = counter + parentCount

            childCount = parentCount * iterateAllBagsInBag(subBagName)
            counter = counter + childCount
    return counter

print(iterateAllBagsInBag('shiny gold bag'))

#part 1
def findSubBagWithName(bag,searchName):
    Found = False
    for subBag in bagDictionary[bag]:
        if(subBag != "no other bag"):    
            subBagName = subBag[2:len(subBag)]
            if(subBagName == searchName):
                Found = True
            if(findSubBagWithName(subBagName,searchName)):
                Found = True
    return Found

#part 1
counter = 0
for bag in bagDictionary:
    if(findSubBagWithName(bag,'shiny gold bag')):
        counter = counter + 1
print(counter)