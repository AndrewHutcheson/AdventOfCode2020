from math import prod

stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
arrivalTime = int(data[0])
busList = data[1]
buses = busList.split(",")

#part1
availableBuses = []
for bus in buses:
    if(bus != "x"):
        availableBuses.append(int(bus))

part1Answers = {}
for bus in availableBuses:
    multiplier = (int(arrivalTime) / int(bus)) + 1
    time = int(bus) * int(multiplier)
    difference = time - arrivalTime
    part1Answers[difference] = int(bus)

print(min(part1Answers)*part1Answers[min(part1Answers)])

#part 2
desiredRemainders = []
count = 0
for bus in buses:
    if bus != "x":
        desiredRemainders.append(count)
    count += 1

index = 0
end = len(desiredRemainders)
offsets = []
while index < end:
    offsets.append(availableBuses[index]-desiredRemainders[index])
    index +=1

#https://brilliant.org/wiki/chinese-remainder-theorem/
#The Chinese remainder theorem is a theorem which gives a unique solution to simultaneous linear congruences
#with coprime moduli. In its basic form, the Chinese remainder theorem will determine a number p that, when 
#divided by some given divisors, leaves given remainders. 
#our given divisors are the bus numbers. 
#our given remainders are calulated above as described in the problem statement.

#I have never encountered this theorem before. I used an implementation from r0f1 as my goal this year is to learn Python although I do like advanced math.
#https://github.com/r0f1/adventofcode2020/blob/master/day13/main.py
b = [busTime - (arrivalTime % busTime) for busTime in availableBuses]
def crt(ns, bs):
    N = prod(ns)
    x = sum(b * (N // n) * pow(N // n, -1, n) for b, n in zip(bs, ns))
    return x % N

print(crt(availableBuses, offsets))