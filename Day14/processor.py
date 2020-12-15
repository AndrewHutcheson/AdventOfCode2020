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


def replacement(addressList,position,x):
    returnAddressList = []
    for address in addressList:
        address2 = address
        address2 = address2[:position] + str(x) + address2[position+1:]
        returnAddressList.append(address2)
    return returnAddressList

def part2():
    masterAddressList = {}
    #m = 0 #used in debugging
    for row in data:
        command = row.split(" = ")
        if(command[0] == "mask"):
            mask = command[1]
        else:
            address = str(command[0][4:len(command[0])-1])
            binaryAddress = str(bin(int(address)).replace("0b", "")).zfill(36)
            value = int(command[1])

            #First, let's replace all the positions that are a 1 or 0 in the mask
            n = 0
            for position in mask:
                if(position == "1"):
                    binaryAddress = binaryAddress[:n] + position + binaryAddress[n+1:]
                n += 1
            
            #next lets tackle the ones that are an X in the mask
            subAddressList = [binaryAddress]
            n = 0
            for position in mask:
                if(position == "X"):
                    subAddressList0 = replacement(subAddressList,n,0)
                    subAddressList1 = replacement(subAddressList,n,1)
                    subAddressList = subAddressList0 + subAddressList1
                n += 1
            
            for address2 in subAddressList:
                decimalAddress = int(address2,2)
                masterAddressList[decimalAddress] = value
            #print("BinA",binaryAddress)
            #print("mask",mask)
        #debugging stuff
        #for newaddress in addressList:
            #print("NewA",str(bin(int(newaddress)).replace("0b", "")).zfill(36))
        #if(m > 0):
            #break
        #m += 1
    return masterAddressList

masterAddressList = part2()
sum = 0        
for masterAddress in masterAddressList:
    value = int(masterAddressList[masterAddress])
    sum += value
print("part2",sum)