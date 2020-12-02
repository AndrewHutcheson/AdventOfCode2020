#part one
stream = open("Input.txt")
numberList = stream.readlines()

for number in numberList:
    for number2 in numberList:
        if(number != number2):
            if(int(number)+int(number2) == 2020):
                print(int(number) * int(number2))
                    

#part two
for number in numberList:
    for number2 in numberList:
        for number3 in numberList:
            if(int(number)+int(number2)+int(number3) == 2020):
                print(int(number) * int(number2) * int(number3))

#