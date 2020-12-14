stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
#there's sometimes an empty newline at the end
for row in data:
    if(row == ""):
        data.remove(row)

addressList = {}

for row in data:
    command = row.split(" = ")
    if(command[0] == "mask"):
        mask = command[1]
    else:
        address = command[0][3:len(command[0])]
        value = int(command[1])
        binaryValue = str(bin(value).replace("0b", "")).zfill(36)
        n = 0
        newBinaryValue = ""
        for position in mask:
            if(position != "X"):
                newBinaryValue = newBinaryValue + position
            else:
                newBinaryValue = newBinaryValue + binaryValue[n]
            n += 1
        newDecimalValue = int(newBinaryValue,2)
        addressList[address] = newDecimalValue
        #print("oldValue =",binaryValue)
        #print("the_Mask =",mask)
        #print("newValue =",newBinaryValue)
        
sum = 0        
for address in addressList:
    value = int(addressList[address])
    sum += value

print(sum)