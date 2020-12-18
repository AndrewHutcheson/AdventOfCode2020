stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
#there's sometimes an empty newline at the end
newData = []
for row in data:
    if(row == ""):
        data.remove(row)
    else:
        newData.append(row.replace(" ",""))
data = newData

#first evaluate parenthesis with recursion.
#then go left to right.

#things to try
#split by operator
#
def evaluateLine(line):
    solution = 0
    for char in line:
        if(char == "+"):
            pass #get the left and right sides of this expression and evaluate
        elif(char == "*"):
            pass #get the left and right sides of this expression and evaluate
        elif(char == "("):
            pass #get whats inside the parenthesis and put it recursively back into this function
        elif(char == ")"):
            pass
        else:
            pass #this is a number, so I can assign it to my left or right operand
    return solution
