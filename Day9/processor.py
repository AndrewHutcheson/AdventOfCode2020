stream = open("input.txt")
lines = stream.readlines()

values = []
n = 0

#part 1
for line in lines:
    values.append(int(line))
    valid = False
    if n > 24: #skip the preamble
        for i in range(1,26): #range 1-26 is the numbers 1-25
            for j in range(1,26):
                if i != j: #because we need two distinct numbers
                    if(values[n-i]+values[n-j]==values[n]):
                        valid = True
    
    if (not valid) and (n > 24):
        print("Part 1: row",n+1,"(",values[n],") is",valid)
        part2Target = values[n]
        break
    n += 1

#part 2
n = 0
values = []
numbers = []
for line in lines:
    values.append(int(line))

while n < len(lines): #for each line I want to start summing everything after it
    runningSum = 0
    m = n
    while m < 575:
        runningSum = runningSum + int(lines[m])
        numbers.append(int(lines[m]))
        if(runningSum == part2Target):
            #print("target row is",m+1)
            #print(numbers)
            minimum = min(numbers)
            maximum = max(numbers)
            break
        elif (runningSum > part2Target):
            runningSum = 0
            numbers = []
        m = m + 1
    n = n + 1
print("Part 2 is",minimum + maximum)