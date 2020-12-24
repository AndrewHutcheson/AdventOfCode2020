#additions for part two
import re

def getItemValue(startPos,line):
    line = line.replace('\n',' ')
    startpos = line.find(':',startPos)+1
    endPos = line.find(' ',startPos)
    if(endPos <= startpos): #needed at EOF
        endPos = len(line)-1 
    value = line[startpos:endPos]
    return value

def checkItemValidity(itemType:str,value:str):
    if(itemType=="byr"):
        if(value.isnumeric): 
            if(int(value) >= 1920 and int(value) <=2002):
                return True
    if(itemType=="iyr"):
        if(value.isnumeric): 
            if(int(value) >= 2010 and int(value) <=2020):
                return True
    if(itemType=="eyr"):
        if(value.isnumeric): 
            if(int(value) >= 2020 and int(value) <=2030):
                return True
    if(itemType=="hgt"):
        if(value[len(value)-2:len(value)] in ['cm','in']):
            units = value[len(value)-2:len(value)]
            amount = value[0:len(value)-2]
            if(units=='in'):
                if((int(amount) >= 59) and (int(amount) <= 76)):
                    return True
            if(units=='cm'):
                if((int(amount) >= 150) and (int(amount) <= 193)):
                    return True
    if(itemType=="hcl"):
        if(re.search('#[0-9,a-f]{6}',value) and (len(value) == 7)):
            return True
    if(itemType=="ecl"):
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    if(itemType=="pid"):
        if(re.search('[0-9]{9}',value) and (len(value) == 9)):
            return True
    if(itemType=="cid"):
        return True
    return False


#part one#
stream = open("input.txt")
lines = stream.readlines()

validCount:int = 0
validFields = {'byr':False,'iyr':False,'eyr':False,'hgt':False,'hcl':False,'ecl':False,'pid':False}
#cid omitted from dictionary because missing it is defined as ok

def resetFields():
    global validFields 
    validFields = {'byr':False,'iyr':False,'eyr':False,'hgt':False,'hcl':False,'ecl':False,'pid':False}

def passportIsValid(passport):
    num_missing_values = 0
    for item in validFields:
        if(validFields[item]==False):
            num_missing_values = num_missing_values + 1
    if(num_missing_values > 0):
        return False
    else:
        return True

lastline = ""

for line in lines:
    lastline = line
    if(line == "\n"):
        if(passportIsValid(validFields)):
            validCount = validCount + 1
        #move on to next line and reset the counter
        resetFields()
    else:
        for item in validFields:
            if(line.find(item)>-1):
                #validFields[item] = True #just this line for part one, the rest of them for part 2
                value = getItemValue(line.find(item), line)
                validFields[item] = checkItemValidity(item,value)

#the last line may not have a \n after it
if(lastline != "\n"):
    for item in validFields:
        if(lastline.find(item)>-1):
            value = getItemValue(lastline.find(item), lastline)
            validFields[item] = checkItemValidity(item,value)
    if(passportIsValid(validFields)): #used for part one
        validCount = validCount + 1

print(validCount)