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

