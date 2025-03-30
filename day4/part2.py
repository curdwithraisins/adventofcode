import re

file = open("./data/input.txt", "r")
matrix = []
diff = 0

while True:
    content = file.readline()
    if not content:
       break
    matrix.append(list(content.rstrip()))

file.close()

def valid(x, y):
    return x - 1 >= 0 and y - 1 >=0 and y + 1 < len(matrix[x]) and x + 1 < len(matrix) 

def up(x, y):
    return 1 if valid(x,y) and matrix[x-1][y-1] == 'M' and matrix[x-1][y+1] == 'M' and matrix[x+1][y+1] == 'S' and matrix[x+1][y-1] == 'S' else 0

def right(x, y):
    return 1 if valid(x,y) and matrix[x-1][y-1] == 'S' and matrix[x-1][y+1] == 'M' and matrix[x+1][y+1] == 'M' and matrix[x+1][y-1] == 'S' else 0

def down(x, y):
    return 1 if valid(x,y) and matrix[x-1][y-1] == 'S' and matrix[x-1][y+1] == 'S' and matrix[x+1][y+1] == 'M' and matrix[x+1][y-1] == 'M' else 0

def left(x, y):
    return 1 if valid(x,y) and matrix[x-1][y-1] == 'M' and matrix[x-1][y+1] == 'S' and matrix[x+1][y+1] == 'S' and matrix[x+1][y-1] == 'M' else 0

for indx, line in enumerate(matrix):
    for indy, value in enumerate(line):
        if value == 'A':
            if up(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if right(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if down(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if left(indx, indy) == 1:
                print(indx, indy)
                diff += 1

print(diff)