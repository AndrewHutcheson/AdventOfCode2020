from collections import Counter

stream = open("input.txt")
lines = stream.readlines()

adapters = [0] #for the initial port rated at 0
differences = []

for line in lines:
    if(line.strip("\n").isnumeric()):
        adapters.append(int(line.strip("\n")))

adapters.sort()
adapters.append(adapters[-1] + 3) #for the device itself

index = 0

while index <= len(adapters)-2:
    differences.append(adapters[index+1]-adapters[index])
    index = index + 1

print(Counter(differences)[1]*Counter(differences)[3])

#part 2
arrangements=1
n=0
while n<len(adapters):
    #If you chave a chain of *consecutive* adapters then you can use the length of the chain to figure out the multiplier (keeping in mind the problem input constraint that gaps are either 1 or 3)
        #being consecutive, we know the limit of how many can be removed before we hit the max gap of 3
    #3 consecutive adapters means two possibilities where one can be removed so we multiply by two
    if (n<len(adapters)-3 and adapters[n]+2==adapters[n+2] and adapters[n]+3!=adapters[n+3]) or (n==len(adapters)-3 and adapters[n]+2==adapters[n+2]):
        arrangements*=2
        n+=3
    #4 consecutive adapters means 4 possibilities where one or more can be removed so we multiple by 4
    elif (n<len(adapters)-4 and adapters[n]+3==adapters[n+3] and adapters[n]+4!=adapters[n+4]) or (n==len(adapters)-4 and adapters[n]+3==adapters[n+3]):
        arrangements*=4
        n+=4
    #5 consecutive adapters means 7 possibilities where one or more can be removed so we multiply by 7
    elif (n<len(adapters)-5 and adapters[n]+4==adapters[n+4] and adapters[n]+5!=adapters[n+5]) or (n==len(adapters)-5 and adapters[n]+4==adapters[n+4]):
        arrangements*=7
        n+=5
    #note that the problem constraint doesn't explicitly say it but as confirmed by other AoC users, the maximum consecutive adapters is 5
    #you can verify these 3 multipliers easily enough by hand*, if there are more than 5 consecutive adapters then you'll need to recognize this is actually a tribonnaci sequence
    else:
        n+=1

print(arrangements)

#*
#Case of 3 consecutive, say [88,89,90]
#we need the total ways to get from 88 to 90 
#   [88,89,90]
#   [88,90]
#   2 total ways

#Case of 4 consecutive, say [13,14,15,16]
#we need the total ways to get from 88 to 90 
#   [13,14,15,16]
#   [13,15,16]
#   [13,14,16]
#   [13,16]
#   4 total ways

#Case of 5 consecutive, say [59,60,61,62,63]
#   [59,60,61,62,63]
#   [59,60,63]
#   [59,61,63]
#   [59,62,63]
#   [59,61,63]
#   [59,60,61,63]
#   [59,60,62,63]
#   7 total ways (keeping the max constraint of 3 jolt difference)