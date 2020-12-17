stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
#there's sometimes an empty newline at the end
for row in data:
    if(row == ""):
        data.remove(row)

#note 1: if each cube only considers it's neighbors then after 6 cycles I shouldn't be more than plus or minue 6 away from the initial 8x8 grid. This gives [0-6 to 7+6] or [-6 to 13]

#part 1
    rows = len(data)
    columns = len(data[0])
    iterations = 6
    expandedSpace = 2*iterations #*2 for both directions

    grid = [[['.' for _ in range(columns + expandedSpace)] for _ in range(rows + expandedSpace)] for _ in range(1 + expandedSpace)] #we start with 8x8x1 which is why z just is one


#populate the initial state
for x, row in enumerate(data):
    for y, column in enumerate(row):
        grid[iterations][x+iterations][y+iterations] = column

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
    inactiveNeighborCount = 0
    for x in range(point[0]-1,point[0]+1):
        for y in range(point[1]-1,point[1]+1):
            for z in range(point[2]-1,point[2]+1):
                try:
                    if not (x == y == z == 0): #this is the point itself, not a neighbor
                        if(inputGrid[x][y][z] == "#"):
                            activeNeighborCount += 1
                        else:
                            inactiveNeighborCount += 1
                except IndexError: #because my point[n]+1/-1 might hit the edge of my #3Dspace
                    pass
    return activeNeighborCount

iteration = 1
while iteration <= iterations:
    nextGrid = grid.copy()
    for iz in range (1 + expandedSpace):
        for iy in range(rows + expandedSpace):
            for ix in range(columns + expandedSpace):
                point = [ix,iy,iz]
                if(x == "#"):
                    if(countActiveNeighbors(point,grid) == 2) or (countActiveNeighbors(point,grid) == 3):
                        pass #remain active
                    else:
                        nextGrid[iz][iy][ix] = "."
                else:
                    if(countActiveNeighbors(point,grid) == 3):
                        nextGrid[iz][iy][ix] = "#"
                    else:
                        pass #remain inactive
    
    grid = nextGrid.copy()
    print("Loop #",iteration,"-",countActiveCells(grid))
    iteration += 1