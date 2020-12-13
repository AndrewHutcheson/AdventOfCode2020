import math

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
        availableBuses.append(bus)

part1Answers = {}
for bus in availableBuses:
    multiplier = (int(arrivalTime) / int(bus)) + 1
    time = int(bus) * int(multiplier)
    difference = time - arrivalTime
    part1Answers[difference] = int(bus)

print(min(part1Answers)*part1Answers[min(part1Answers)])

