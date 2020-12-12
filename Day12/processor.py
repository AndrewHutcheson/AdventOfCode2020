stream = open("input.txt")
lines = stream.read()
instructions = lines.split("\n")
#there's sometimes an empty newline at the end
for row in instructions:
    if(row == ""):
        instructions.remove(row)

#first let's see if we can define the constraints a little more. Are rotations in 45 or 90 degrees or do I need to do some trig?
#for instruction in instructions:
    #if(instruction[0]=="R" or instruction[0]=="L"):
        #print(instruction)
#ok that checks out. All are multiples of 90.

x = 0
y = 0
#1 is East, 2 is South, 3 is West and 4 is North
curDirection = 1
for step in instructions:
    dir = step[0]
    qty = int(step[1:])
    if(dir == "N"):
        y += qty
    elif(dir == "S"):
        y -= qty
    elif(dir == "E"):
        x += qty
    elif(dir == "W"):
        x -= qty
    elif(dir == "F"):
        if(curDirection == 1):
            x += qty
        elif(curDirection == 3):
            x -= qty
        elif(curDirection == 4):
            y += qty
        elif(curDirection == 2):
            y -= qty
    elif(dir == "R"):
        if(qty == 90):
            curDirection += 1
        elif(qty == 180):
            curDirection += 2
        elif(qty == 270):
            curDirection += 3
        if(curDirection > 4):
            curDirection = curDirection - 4
    elif(dir == "L"):
        if(qty == 90):
            curDirection += 3
        elif(qty == 180):
            curDirection += 2
        elif(qty == 270):
            curDirection += 1
        if(curDirection > 4):
            curDirection = curDirection - 4
    #print(curDirection)
print(abs(x)+abs(y))

#part 2, x and y are now the waypoint's coordinates
x = 10
y = 1
shipX = 0
shipY = 0
#1 is East, 2 is South, 3 is West and 4 is North
for step in instructions:
    dir = step[0]
    qty = int(step[1:])
    if(dir == "N"):
        y += qty
    elif(dir == "S"):
        y -= qty
    elif(dir == "E"):
        x += qty
    elif(dir == "W"):
        x -= qty
    elif(dir == "F"):
        shipX += qty*x
        shipY += qty*y
    elif(dir == "L"):
        if(qty == 90):
            temp = x
            x = -y
            y = temp
        elif(qty == 180):
            x = -x
            y = -y
        elif(qty == 270):
            temp = x
            x = y
            y = -temp
    elif(dir == "R"):
        if(qty == 90):
            temp = x
            x = y
            y = -temp
        elif(qty == 180):
            x = -x
            y = -y
        elif(qty == 270):
            temp = x
            x = -y
            y = temp

print(abs(shipX)+abs(shipY))