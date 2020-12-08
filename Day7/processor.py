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

def countAllBagsInBagWithName(bag,searchName):
    counter = 0
    for subBag in bagDictionary[bag]:
        if(subBag != "no other bag"):    
            subBagName = subBag[2:len(subBag)]
            parentCount = int(subBag[0:2])
            if(subBagName == searchName):
                counter = counter + parentCount
            
    return counter

#part 1
counter = 0
for bag in bagDictionary:
    counter = counter + countAllBagsInBagWithName(bag,'shiny gold bag')
print(counter)