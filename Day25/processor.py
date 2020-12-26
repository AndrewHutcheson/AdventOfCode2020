def findLoopSize(public_key):
    startValue = 1
    for number in range(1, 100000000):
        startValue = startValue * 7
        startValue = startValue % 20201227
        if startValue == public_key:
            return number

def find_encryption_key(key, loopSize):
    startValue = 1
    for number in range(1, loopSize + 1):
        startValue = startValue * key
        startValue = startValue % 20201227
    return startValue

doorKey = 7573546
cardKey = 17786549
cardLoopSize = findLoopSize(cardKey)
encryptionKey = find_encryption_key(doorKey, cardLoopSize)
print("Part1:",encryptionKey)

