stream = open("input.txt")
lines = stream.readlines()

class bagObject:
    def __init__(self, color):
        self.color = color
        self.children = []
        
    def addChild(self,child):
        self.children.append(child)

def getOcurrencesOfChild(children,search):
    for child in children:
        if(child.find(search)>-1):
            return int(child[0:2])
    return 0

bagContents = dict()

for line in lines:
    temp = line.strip("\n").split("contain")
    parent = temp[0][0:len(temp[0])-1] #subtract one to remove the trailing space
    children = temp[1].strip(".").split(",")
    bag = bagObject(parent)
    for child in children:
        bag.addChild(child[1:len(child)]) #and here we have a leading space
    bagContents[parent] = bag

def makeStringPlural(string):
    if string[-1:len(string)] != "s":
        return string + "s"
    else:
        return string

def makeStringSingular(string):
    if string[-1:len(string)] == "s":
        return string[0:len(string)-1]
    else:
        return string

def searchInBag(bag,search):
    returnValue = 0
    for child in bag.children: #empty bag        
        if(child.find(search)>-1): #the search bag has been found, just this at top level should be 20 total
            returnValue = returnValue + getOcurrencesOfChild(bag.children,search)
        elif(child != "no other bags"): #not the search bag but not empty
            newBagColor = makeStringPlural(child[2:len(child)])
            newBag = bagContents[newBagColor]
            #print("getOcurrencesOfChild(bag.children,search)",getOcurrencesOfChild(bag.children,search))
            returnValue = getOcurrencesOfChild(bag.children,makeStringSingular(newBagColor)) * searchInBag(newBag,search)
        else:
            returnValue = 0
    return returnValue

def part1():
    counter = 0
    for bag in bagContents:
        counter = counter + searchInBag(bagContents[bag],"shiny gold bags")
        #print(searchInBag(bagContents[bag],"shiny gold bag"))
    print("part 1 is",counter)
part1()

#test case
#print(searchInBag(bagContents['drab magenta bags'] ,"shiny gold bag")) #should give at least 16

#part 2
def countInBag(bag):
    returnValue = 0
    for child in bag.children: #empty bag        
        if(child == "no other bags"): #not the search bag but not empty
            returnValue = 1
        else:
            childBagName = makeStringPlural(child[2:len(child)])
            childBagNumber = getOcurrencesOfChild(bag.children,child)
            returnValue = returnValue + childBagNumber * countInBag(bagContents[childBagName])
    return returnValue

def part2():
    counter = 0
    for bag in bagContents["shiny gold bags"].children:
        counter = counter + int(bag[0:2])*countInBag(bagContents[bag[2:len(bag)]])
    print("part 2 is",counter)
part2()    