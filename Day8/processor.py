stream = open("input.txt")
lines = stream.readlines()

accumulator = 0
commandsUsed = []
commands = []

for line in lines:
    command = line.strip("\n").split(" ")
    operation = command[0]
    argument = command[1]
    commands.append({operation:argument})
    commandsUsed.append(False)

currentLine = 0
for command in commands:
    if(commandsUsed[currentLine]):
        break
    else:
        commandsUsed[currentLine] = True
        operation = list(commands[currentLine].keys())[0]
        argument = int(commands[currentLine].get(operation))

        if(operation == "acc"):
            accumulator += argument
            currentLine += 1
        elif(operation == "jmp"):
            currentLine += argument
        elif(operation == "nop"):
            currentLine += 1

print(accumulator)

#part 2
for changedRow in range(1,len(lines)):
    accumulator = 0
    rowHasBeenChanged = []
    n = 0
    EOF = False
    while n not in rowHasBeenChanged:
        rowHasBeenChanged.append(n)
        operation = list(commands[n].keys())[0]
        argument = int(commands[n].get(operation))
        #acc doesnt change but op changed to jmp and jmp changes to op
        if changedRow == n: #if this row is the target for this iteration then switch the op on that row
            if operation == 'jmp':
                operation = 'nop'
            elif operation == 'nop':
                operation = 'jmp'
        if operation == 'nop': 
            n += 1
            continue
        elif operation == 'jmp':
            n += int(argument)
        elif operation == 'acc':
            n += 1
            accumulator += int(argument)
        #if we get to the last line properly then set EOF so we break the loop and stop trying
        if n == len(lines): 
            EOF = True
            break
    if EOF:
        break

print(accumulator)