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

#make a test case:
#dim red bags contain 2 dim salmon bags, 2 faded orange bags, 5 muted aqua bags.
#print(bagDictionary['dim red bag'])

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

#print(iterateAllBagsInBag('dim red bag'))
print(iterateAllBagsInBag('shiny gold bag'))

#part 1
def findSubBagWithName(bag,searchName):
    found = False
    if(bag == searchName):
        found = True
    else:
        for subBag in bagDictionary[bag]:
            if(subBag != "no other bag"):    
                subBagName = subBag[2:len(subBag)]
                if(subBagName == searchName):
                    found = True
                else:
                    found = findSubBagWithName(subBagName,searchName)
    return found

#part 1
counter = 0
for bag in bagDictionary:
    if(findSubBagWithName(bag,'shiny gold bag')):
        counter = counter + 1
print(counter)