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
        
sum = 0        
for address in addressList:
    value = int(addressList[address])
    sum += value
print("part1",sum)


###########################
########## part 2 #########
###########################
addressList = {}

def replacement(addressList,position,x):
    returnAddressList = []
    for address in addressList:
        address2 = address
        address2 = address2[:position] + str(x) + address2[position+1:]
        returnAddressList.append(address2)
    return returnAddressList

m = 0
for row in data:
    command = row.split(" = ")
    if(command[0] == "mask"):
        mask = command[1]
    else:
        address = str(command[0][4:len(command[0])-1])
        binaryAddress = str(bin(int(address)).replace("0b", "")).zfill(36)
        value = int(command[1])

        subAddressList = [binaryAddress]
        n = 0
        for position in mask:
            if(position == "X"):
                subAddressList0 = replacement(subAddressList,n,0)
                subAddressList1 = replacement(subAddressList,n,1)
                subAddressList = subAddressList0 + subAddressList1
            n += 1
        
        for address in subAddressList:
            decimalAddress = int(address,2)
            addressList[decimalAddress] = value
    #print(len(addressList)) #this checks out
    #if(m > 0):
        #break
    m += 1

sum = 0        
for address in addressList:
    value = int(addressList[address])
    sum += value
print("part2",sum)