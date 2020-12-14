stream = open("input.txt")
lines = stream.read()
seatRows = lines.split("\n")

#there's sometimes an empty newline at the end
for row in seatRows:
    if(row == ""):
        seatRows.remove(row)

#populate input
originalSeats = {}
for r, row in enumerate(seatRows):
    for c, seat in enumerate(row):
        originalSeats[r,c] = seat

def isSeatOccupied(x,y,seats,offset):
    x = x + offset[0]
    y = y + offset[1]
    #if we are at the edge of the plane I want to return False because that imaginary/virtual seat beyond the boundary counts as vacant
    try:
        if(seats[x,y] == "#"):
            return True
        else:
            return False
    except KeyError:
        return False

newSeats = {}
changed = True
iterationCount = 0
while changed:
    for (row, col), seat in originalSeats.items():
        if seat == ".":
            newSeats[row,col] = "."
        elif seat == "L":
            occupied = 0
            for i in range(-1,2): #-1,2 gives -1 to 1
                for j in range(-1,2):
                    if (i == 0) and (j == 0):
                        continue
                    if(isSeatOccupied(row,col,originalSeats,[i,j])):
                        occupied += 1
            if(occupied == 0):
                newSeats[row,col] = "#"
        elif(seat == "#"):
            occupied = 0
            for i in range(-1,2): #-1,2 gives -1 to 1
                for j in range(-1,2):
                    if i == j == 0:
                        continue
                    if(isSeatOccupied(row,col,originalSeats,[i,j])):
                        occupied += 1
            if(occupied >= 4):
                newSeats[row,col] = "L"
    
    if(newSeats == originalSeats):
        changed = False

    originalSeats = newSeats.copy()
    iterationCount += 1

count = 0
for n in originalSeats.values():
    if n == "#":
        count += 1

print("Part 1 iterations:",iterationCount)    
print("Part 1:", count)

###############################################
################### part 2 ####################
###############################################

#ok, now I want a function that keeps searching in that same direction.
def isDirectionOccupied(x,y,seats,offset):
    while True:
        x = x + offset[0]
        y = y + offset[1]

        try:
            if(seats[x,y]=="#"):
                return True
            elif(seats[x,y]=="L"):
                return False
            else: #if its == ".", do the loop again and increment in that direction
                pass
        except KeyError:
            return False

#repopulate input
originalSeats = {}
for r, row in enumerate(seatRows):
    for c, seat in enumerate(row):
        originalSeats[r,c] = seat

newSeats = {}
changed = True
iterationCount = 0
while changed:
    for (row, col), seat in originalSeats.items():
        #print("row",row,"col",col)
        if seat == ".":
            newSeats[row,col] = "."
        elif seat == "L":
            occupied = 0
            for i in range(-1,2): #-1,2 gives -1 to 1
                for j in range(-1,2):
                    if (i == 0) and (j == 0):
                        continue
                    if(isDirectionOccupied(row,col,originalSeats,[i,j])):
                        occupied += 1
            if(occupied == 0):
                newSeats[row,col] = "#"
        elif(seat == "#"):
            occupied = 0
            for i in range(-1,2): #-1,2 gives -1 to 1
                for j in range(-1,2):
                    if (i == 0) and (j == 0):
                        continue
                    if(isDirectionOccupied(row,col,originalSeats,[i,j])):
                        occupied += 1
            if(occupied >= 5):
                newSeats[row,col] = "L"
    
    if(newSeats == originalSeats):
        changed = False

    originalSeats = newSeats.copy()
    iterationCount += 1
    #print(iterationCount)

count = 0
for n in originalSeats.values():
    if n == "#":
        count += 1

print("Part 2 iterations:",iterationCount)    
print("Part 2:", count)