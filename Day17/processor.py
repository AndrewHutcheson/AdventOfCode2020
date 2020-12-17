stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
#there's sometimes an empty newline at the end
for row in data:
    if(row == ""):
        data.remove(row)

#note 1: if each cube only considers it's neighbors then after 6 cycles I shouldn't be more than plus or minue 6 away from the initial 8x8 grid. This gives [0-6 to 7+6] or [-6 to 13]

#note2: 3x3x3, minus the one at the center yields 26 neighbors
def checkNeighbors(point,currentCubeState):
    activeNeightborCount = 0
    inactiveNeightborCount = 0
    for x in range(point[0]-1,point[0]+1):
        for y in range(point[1]-1,point[1]+1):
            for z in range(point[2]-1,point[2]+1):
                try:
                    if not (x == y == z == 0): #this is the point, not a neighbor
                        if(currentCubeState[x][y][z] == 1):
                            activeNeightborCount += 1
                        else:
                            inactiveNeightborCount += 1
                except KeyError: #because my point[n]+1/-1 might hit the edge of my space
                    continue
    #if(activeNeightborCount > 0):
        #print("ANC",activeNeightborCount,x,y,z,"INC",inactiveNeightborCount)
    #else:
        #print("no active neighbors")
    return activeNeightborCount

def countAllActive(cubeState):
    count = 0
    for x in cubeState:
        for y in cubeState[x]:
            for z in cubeState[x][y]:
                if(cubeState.get(x).get(y).get(z) == 1):
                    count += 1
    return count

#create a master array from -6 to 13
keys = range(-6,14)
zDimension = dict.fromkeys(keys,0)
yDimension = dict.fromkeys(keys,zDimension)
masterCubeState = dict.fromkeys(keys,yDimension)

#Read Initial Cube State
z = 0
for x,row in enumerate(data):
    for y,state in enumerate(row):
        if(state=="#"):
            #print("found an active state",x,y,z)
            masterCubeState[x][y][z] = 1

#print(masterCubeState)
print("initial state",countAllActive(masterCubeState))
#iterate 6 times
for cycle in range(1,7):
    nextCubeState = masterCubeState.copy()
    for x in keys:
        for y in keys:
            for z in keys:
                point = [x,y,z]
                numberActive = checkNeighbors(point,masterCubeState)
                if masterCubeState[x][y][z] == 1:
                    if(numberActive == 2) or (numberActive == 3):
                        pass #remains active
                    else: #number active not 2 or 3
                        nextCubeState[x][y][z] = 0
                else:
                    if(numberActive == 3):
                        nextCubeState[x][y][z] = 1
                    else:
                        pass #remains inactive
    masterCubeState = nextCubeState.copy()

    print(countAllActive(masterCubeState))
