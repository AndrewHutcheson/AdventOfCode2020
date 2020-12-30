import re
#process input
#stream = open("sampleInput.txt")
stream = open("input.txt")
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
            returnRule = returnRule + "("
            for sub in subRules:
                nums = sub.split(" ")
                for num in nums:
                    #print(rulesDict[int(num)])
                    returnRule = returnRule + convertToRegex(rulesDict[int(num)])
                returnRule = returnRule + "|"
            returnRule = returnRule[0:len(returnRule)-1] #get rid of last |
            returnRule = returnRule + ")"
        else: #there is no or operator
            nums = rule.split(" ")
            returnRule = returnRule + "("
            for num in nums:
                #print(rulesDict[int(num)])
                returnRule = returnRule + convertToRegex(rulesDict[int(num)])
            returnRule = returnRule + ")"
    return returnRule

for row in rulesDict:
    rule = rulesDict[row]
    if(convertToRegex(rule)[0] == "("):
        regExRules[row] = convertToRegex(rule)[1:len(convertToRegex(rule))-1]
    else:
        regExRules[row] = convertToRegex(rule)

#print(regExRules)
#part 1 I just want rule 0
count = 0
rule = "^" + regExRules[0] + "\Z"
for row in datum:
    #print(re.match(rule,row))
    if(re.match(rule,row)):
        #print(row,"matches",rule)
        count += 1
    else:
        pass#print(row,"does not match",rule)
    #print()

print("part 1:",count)

#part 2
rulesDict[8] = "42 | 42 8"
rulesDict[11] = "42 31 | 42 11 31"
regExRules = {}

def convertToRegexPart2(rule):
    if(rule.find(" 8 ")>-1) or (rule.find(" 11 ")>-1):
        return ""
    returnRule = ""
    if(rule == "a" or rule == "b"):
        returnRule = rule
    else:
        if(rule.find("|") > 0):
            subRules = rule.split(" | ")
            returnRule = returnRule + "("
            for sub in subRules:
                nums = sub.split(" ")
                for num in nums:
                    #print(rulesDict[int(num)])
                    returnRule = returnRule + convertToRegex(rulesDict[int(num)])
                returnRule = returnRule + "|"
            returnRule = returnRule[0:len(returnRule)-1] #get rid of last |
            returnRule = returnRule + ")"
        else: #there is no or operator
            nums = rule.split(" ")
            returnRule = returnRule + "("
            for num in nums:
                #print(rulesDict[int(num)])
                returnRule = returnRule + convertToRegex(rulesDict[int(num)])
            returnRule = returnRule + ")"
    return returnRule

for row in rulesDict:
    rule = rulesDict[row]
    if(convertToRegexPart2(rule)[0] == "("):
        regExRules[row] = convertToRegexPart2(rule)[1:len(convertToRegexPart2(rule))-1]
    else:
        regExRules[row] = convertToRegexPart2(rule)

count = 0
rule = "^" + regExRules[0] + "\Z"
for row in datum:
    #print(re.match(rule,row))
    if(re.match(rule,row)):
        #print(row,"matches",rule)
        count += 1
    else:
        pass#print(row,"does not match",rule)
    #print()

print("part 2:",count)        