
def getPositionN(iterations):
    lastNum = 0
    curNum = 0
    numbers = {6: 0, 3: 1, 15: 2, 13: 3, 1: 4, 0: 5}
    turn = 5
    while turn < iterations - 1:
        curNum = lastNum
        if curNum not in numbers.keys():
            lastNum = 0
        else:
            lastNum = turn - numbers[curNum]
        numbers[curNum] = turn
        turn += 1
    return lastNum

print("part 1:",getPositionN(2020))
print("part 2:",getPositionN(30000000))