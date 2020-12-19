import re
#process input
stream = open("sampleInput.txt")
#stream = open("input.txt")
lines = stream.read()
data = lines.split("\n\n")
rules = data[0].split("\n")
datum = data[1].split("\n")
for row in datum:
    if(row == ""):
        datum.remove(row)#there's sometimes an empty newline at the end

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

#Part 1 goal is the number of messages that completely match rule 0, or rulesDict[0]
#for each rule, I want to build a regular expression
    #I want a recursive algorithm to do this

rulesDict = {}
for rule in rules:
    parts = rule.split(": ")
    ruleNum = int(parts[0])
    ruleItself = parts[1]
    if(ruleItself == '"a"'): #this is a hacky way of doing this without more regEx's
        ruleItself = "a"
    if(ruleItself == '"b"'):
        ruleItself = "b"
    rulesDict[ruleNum] = ruleItself

regExRules = {} #sorted just to make reading debugging output easier

def convertToRegex(rule):
    returnRule = ""
    if(rule == "a" or rule == "b"):
        returnRule = rule
    else:
        if(rule.find("|") > 0):
            subRules = rule.split(" | ")
            returnRule = returnRule + "["
            for sub in subRules:
                nums = sub.split(" ")
                for num in nums:
                    #print(rulesDict[int(num)])
                    returnRule = returnRule + convertToRegex(rulesDict[int(num)])
                returnRule = returnRule + "|"
            returnRule = returnRule[0:len(returnRule)-1] #get rid of last |
            returnRule = returnRule + "]"
        else: #there is no or operator
            nums = rule.split(" ")
            returnRule = returnRule + "["
            for num in nums:
                #print(rulesDict[int(num)])
                returnRule = returnRule + convertToRegex(rulesDict[int(num)])
            returnRule = returnRule + "]"
    return returnRule

for row in rulesDict:
    rule = rulesDict[row]
    regExRules[row] = convertToRegex(rule)

#test case
#print(convertToRegex("23 105 | 105 23")) #this is 104:
#print()
#print(convertToRegex("104 105")) #this is 104:
#print()
print(regExRules)

for row in datum:
    for rule in regExRules:
        if(re.match(regExRules[rule],row)):
            print(row,"matches",regExRules[rule])
        else:
            print(row,"does not match",regExRules[rule])