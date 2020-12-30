stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
newData = []
for row in data:
    if(row == ""):
        data.remove(row)#there's sometimes an empty newline at the end
    else:
        newData.append(row.replace(" ",""))
data = newData

def evaluateLine(line):
    operands = list()
    operators = list()
    index = 0
    end = len(line)
    
    while index<end:
        if line[index] == "+":
            operators.append("+")
        elif line[index] == "*":
            operators.append("*")
        elif line[index] == ")":
            return (index+1,operands.pop())
        elif line[index] == "(":
            to_add,result = evaluateLine(line[index+1:])
            if operators != []:
                op = operators.pop()
                op1 = operands.pop()
                if(op == "+"):
                    result = op1 + result
                else:
                    result = op1 * result
            operands.append(result)
            index += to_add
        else:
            if operators == []:
                operands.append(int(line[index]))
            else:
                op = operators.pop()
                op1 = operands.pop()
                op2 = int(line[index])
                if(op == "+"):
                    result = op1 + op2
                else:
                    result = op1 * op2
                operands.append(result)
        index += 1

    if operators == []:
        return operands.pop()
    else:
        op = operators.pop()
        op1 = operands.pop()
        op2 = operands.pop()
        if(op == "+"):
            result = op1 + op2
        else:
            result = op1 * op2
        return result

grandTotal = 0
for line in data:
    grandTotal += evaluateLine(line)
print("part1:",grandTotal)

#now for part 2, same rules but we have operator precedence
def evaluateLinePart2(line):
    operands = list()
    operators = list()
    index = 0
    end = len(line)
    
    while index<end:
        if line[index] == "+":
            operators.append("+")
        elif line[index] == "*":
            operators.append("*")
        elif line[index] == ")":
            if operators != []:
                for op in operators:
                    op1 = operands.pop()
                    op2 = operands.pop()
                    if(op == "+"):
                        result = op1 + op2
                    else:
                        result = op1 * op2
                    operands.append(result)
            return (index+1,operands.pop())
        elif line[index] == "(":
            to_add,result = evaluateLinePart2(line[index+1:])
            if operators != []:
                if operators[-1] == "+":
                    op = operators.pop()
                    op1 = operands.pop()
                    if(op == "+"):
                        result = op1 + result
                    else:
                        result = op1 * result
            operands.append(result)
            index += to_add
        else:
            if(operators == []):
                operands.append(int(line[index]))
            else:
                if(operators[-1]=="+"):
                    op = operators.pop()
                    op1 = operands.pop()
                    op2 = int(line[index])
                    if(op == "+"):
                        result = op1 + op2
                    else:
                        result = op1 * op2
                    operands.append(result)
                else:
                    operands.append(int(line[index]))
        index += 1

    if (operators != []):
        for op in operators:
            op1 = operands.pop()
            op2 = operands.pop()
            if(op == "+"):
                result = op1 + op2
            else:
                result = op1 * op2
            operands.append(result)

    return operands.pop()

grandTotal = 0
for line in data:
    grandTotal += evaluateLinePart2(line)
print("part2:",grandTotal)