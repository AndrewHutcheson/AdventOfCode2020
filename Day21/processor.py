stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
#there's sometimes an empty newline at the end
for row in data:
    if(row == ""):
        data.remove(row)

possiblyIsIn = {}
for row in data:
    temp = row.split(" (contains")
    ingredients = temp[0].split(" ")
    allergens = temp[1][1:len(temp[1])-1].split(", ")
    
    for allergen in allergens:
        if allergen not in possiblyIsIn:
            possiblyIsIn[allergen] = [] 
            possiblyIsIn[allergen].append(ingredients)
        else:
            possiblyIsIn[allergen].append(ingredients)

for possibility in possiblyIsIn:
    print(possibility)
    print(possiblyIsIn[possibility])
    break