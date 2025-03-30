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

def up(x, y):
    return 1 if x > 2 and matrix[x-1][y] == 'M' and matrix[x-2][y] == 'A' and matrix[x-3][y] == 'S' else 0

def up_right(x, y):
    return 1 if x > 2 and y < len(matrix[x]) - 3 and matrix[x-1][y+1] == 'M' and matrix[x-2][y+2] == 'A' and matrix[x-3][y+3] == 'S' else 0

def right(x, y):
    return 1 if y < len(matrix[x]) - 3 and matrix[x][y+1] == 'M' and matrix[x][y+2] == 'A' and matrix[x][y+3] == 'S' else 0

def right_down(x, y):
    return 1 if x < len(matrix) - 3 and y < len(matrix[x]) - 3 and matrix[x+1][y+1] == 'M' and matrix[x+2][y+2] == 'A' and matrix[x+3][y+3] == 'S' else 0

def down(x, y):
    return 1 if x < len(matrix) - 3 and matrix[x+1][y] == 'M' and matrix[x+2][y] == 'A' and matrix[x+3][y] == 'S' else 0

def down_left(x, y):
    return 1 if x < len(matrix) - 3 and y > 2 and matrix[x+1][y-1] == 'M' and matrix[x+2][y-2] == 'A' and matrix[x+3][y-3] == 'S' else 0

def left(x, y):
    return 1 if y > 2 and matrix[x][y-1] == 'M' and matrix[x][y-2] == 'A' and matrix[x][y-3] == 'S' else 0

def left_up(x, y):
    return 1 if y > 2 and x > 2 and matrix[x-1][y-1] == 'M' and matrix[x-2][y-2] == 'A' and matrix[x-3][y-3] == 'S' else 0

for indx, line in enumerate(matrix):
    for indy, value in enumerate(line):
        if value == 'X':
            if up(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if up_right(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if right(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if right_down(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if down(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if down_left(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if left(indx, indy) == 1:
                print(indx, indy)
                diff += 1
            if left_up(indx, indy) == 1:
                print(indx, indy)
                diff += 1

print(diff)