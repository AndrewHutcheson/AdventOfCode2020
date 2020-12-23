stream = open("input.txt")
lines = stream.read()
data = lines.split("\n")
#there's sometimes an empty newline at the end
for row in data:
    if(row == ""):
        data.remove(row)

class tile:
    def __init__(self):
        tileNumber = ""
    
    def getTileImage():
        pass
    
    def getTileTopRow():
        pass

    def getTileBottomRow():
        pass

    

