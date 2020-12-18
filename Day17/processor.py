import copy

stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
#there's sometimes an empty newline at the end
for row in data:
    if(row == ""):
        data.remove(row)

#part 1
    rows = len(data)
    columns = len(data[0])
    iterations = 6
    expandedSpace = 2*iterations # I multiply by 2 for both directions getting another potential row each iteration

    grid = [[['.' for x in range(columns + expandedSpace)] for y in range(rows + expandedSpace)] for z in range(1 + expandedSpace)] #we start with 8x8x1 which is why z just is one


#populate the initial state
for y, row in enumerate(data):
    for x, column in enumerate(row):
        grid[iterations][y+iterations][x+iterations] = column #start at [iterations] because I shift my initial state to the center so it can expand outward

def countActiveCells(inputGrid):
    count = 0
    for z in inputGrid:
        for y in z:
            for x in y:
                if(x == "#"):
                    count += 1
    return count

def countActiveNeighbors(point,inputGrid):
    activeNeighborCount = 0
    for z in range(point[0]-1,point[0]+2):
        for y in range(point[1]-1,point[1]+2):
            for x in range(point[2]-1,point[2]+2):
                try:
                    if not((z == point[0]) and (y == point[1]) and (x == point[2])): #this is the point itself, not a neighbor
                        if(inputGrid[z][y][x] == "#"):
                            activeNeighborCount += 1
                except IndexError: #because my point[n]+1/-1 might hit the edge of my 3Dspace, in which case it's an inactive cell
                    pass
    return activeNeighborCount

#test cases
#print(grid[6][12][11]) #yep 
#print(countActiveNeighbors([6,12,11],grid)) #checks out.
print("3D Loop # 0","-",countActiveCells(grid)) 

iteration = 1
while iteration <= iterations:
    nextGrid = copy.deepcopy(grid) #compound objects, like a list of lists, use references on shallow copies so I need a deep copy
    for iz in range (1 + expandedSpace):
        for iy in range(rows + expandedSpace):
            for ix in range(columns + expandedSpace):
                point = [iz,iy,ix]
                #print(countActiveNeighbors(point,grid))
                if(grid[iz][iy][ix] == "#"):
                    if(countActiveNeighbors(point,grid) == 2) or (countActiveNeighbors(point,grid) == 3):
                        pass #remain active
                    else:
                        nextGrid[iz][iy][ix] = "."
                else:
                    if(countActiveNeighbors(point,grid) == 3):
                        nextGrid[iz][iy][ix] = "#"
                    else:
                        pass #remain inactive
    
    grid = copy.deepcopy(nextGrid)
    print("3D Loop #",iteration,"-",countActiveCells(grid))
    iteration += 1

###############################
########### part 2 ############
###############################

def count4DActiveCells(inputGrid):
    count = 0
    for w in inputGrid:
        for z in w:
            for y in z:
                for x in y:
                    if(x == "#"):
                        count += 1
    return count

def count4DActiveNeighbors(point,inputGrid):
    activeNeighborCount = 0
    for w in range(point[0]-1,point[0]+2):
        for z in range(point[1]-1,point[1]+2):
            for y in range(point[2]-1,point[2]+2):
                for x in range(point[3]-1,point[3]+2):
                    try:
                        if not((w == point[0]) and (z == point[1]) and (y == point[2]) and (x == point[3])): #this is the point itself, not a neighbor
                            if(inputGrid[w][z][y][x] == "#"):
                                activeNeighborCount += 1
                    except IndexError: #because my point[n]+1/-1 might hit the edge of my 3Dspace, in which case it's an inactive cell
                        pass
    return activeNeighborCount

rows = len(data)
columns = len(data[0])
iterations = 6
expandedSpace = 2*iterations # I multiply by 2 for both directions getting another potential row each iteration

grid4D = [[[['.' for x in range(columns + expandedSpace)] for y in range(rows + expandedSpace)] for z in range(1 + expandedSpace)] for w in range(1 + expandedSpace)] #we start with 8x8x1 which is why z just is one


#populate the initial state
for y, row in enumerate(data):
    for x, column in enumerate(row):
        grid4D[iterations][iterations][y+iterations][x+iterations] = column #start at [iterations][iterations] because I shift my initial state to the center so it can expand outward

#test cases
#print(grid[6][12][11]) #yep 
#print(countActiveNeighbors([6,12,11],grid)) #checks out.
print("4D Loop # 0","-",count4DActiveCells(grid4D)) 

iteration = 1
while iteration <= iterations:
    next4DGrid = copy.deepcopy(grid4D) #compound objects, like a list of lists, use references on shallow copies so I need a deep copy
    for iw in range (1 + expandedSpace):
        for iz in range (1 + expandedSpace):
            for iy in range(rows + expandedSpace):
                for ix in range(columns + expandedSpace):
                    point = [iw,iz,iy,ix]
                    #print(countActiveNeighbors(point,grid))
                    if(grid4D[iw][iz][iy][ix] == "#"):
                        if(count4DActiveNeighbors(point,grid4D) == 2) or (count4DActiveNeighbors(point,grid4D) == 3):
                            pass #remain active
                        else:
                            next4DGrid[iw][iz][iy][ix] = "."
                    else:
                        if(count4DActiveNeighbors(point,grid4D) == 3):
                            next4DGrid[iw][iz][iy][ix] = "#"
                        else:
                            pass #remain inactive
    
    grid4D = copy.deepcopy(next4DGrid)
    print("4D Loop #",iteration,"-",count4DActiveCells(grid4D))
    iteration += 1 