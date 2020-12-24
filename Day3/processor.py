stream = open("input.txt")
lines = stream.readlines()

def is_tree(char):
    if(char == "#"):
        return True
    else:
        return False

#define some parameters for the problem
def calculate_slope(slope_x,slope_y):
    rows = len(lines)
    columns = len(lines[1])

    x = 0
    y = 0
    trees = 0

    while y <= rows-1:
        current_position = lines[y][x]
        if(is_tree(current_position)):
            trees = trees + 1
        y = y + slope_y
        x = x + slope_x
        if(x >= columns-1):
            x = x - (columns-1)

    return (trees)

#part 1
print(calculate_slope(3,1))

#part 2#
a = calculate_slope(1,1)
b = calculate_slope(3,1)
c = calculate_slope(5,1)
d = calculate_slope(7,1)
e = calculate_slope(1,2)

print(a*b*c*d*e)