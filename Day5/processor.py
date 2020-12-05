stream = open("input.txt")
lines = stream.readlines()

def decode_seat(rowString):
    #first seven characters give me the row
    rowString = rowString.replace("F","0")
    rowString = rowString.replace("B","1")
    rowString = rowString.replace("L","0")
    rowString = rowString.replace("R","1")
    return rowString

seats = []
for line in lines:
    seats.append(decode_seat(line))

max = 0
for seat in seats:
    if(int(seat) > int(max)):
        max = seat
#print(max[0:7])

row = decode_seat(max[0:7])
row = int(row,2)
#print(row)

#I need the column
#last 3 characters
column = max[-4:len(max)-1]
column = int(decode_seat(column),2)
#print(column)

print(row*8+column)

#part 2
#convert every row to its seatID
seatNums = []
for seat in seats:
    row = decode_seat(seat[0:7])
    row = int(row,2)
    column = column = seat[-4:len(seat)-1]
    column = int(decode_seat(column),2)
    seatNums.append(row*8+column)

seatNums.sort()
#print(seatNums)

firstSeat = seatNums[0]
lastSeat = seatNums[len(seatNums)-1]

currentSeat = firstSeat + 1 #its not the first or last as given in problem statement
while currentSeat < lastSeat:
    if not (currentSeat in seatNums):
        print(currentSeat)
    currentSeat = currentSeat + 1
