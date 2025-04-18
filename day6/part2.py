import re

file = open("./data/input.txt", "r")
path = []

while True:
    content = file.readline()
    if not content:
       break
    path.append(list(content.rstrip()))

file.close()

i = 0
j = 0
while i < len(path):
    if '^' in path[i]:
        j = path[i].index('^')
        path[i][j] = 'A'
        break
    if '>' in path[i]:
        j = path[i].index('>')
        path[i][j] = 'B'
        break
    if '<' in path[i]:
        j = path[i].index('<')
        path[i][j] = 'C'
        break
    if 'v' in path[i]:
        j = path[i].index('v')
        path[i][j] = 'D'
        break
    i += 1

num = 1
obs = 0
current = path[i][j]

while i >=0 and i < len(path) and j >=0 and j < len(path[i]):
    print(path)
    print(current)
    print(i,j)
    if path[i][j] == '#':
        if current == 'A':
            j += 1
        elif current == 'B':
            i += 1
        elif current == 'C':
            j -= 1
        elif current == 'D':
            i -= 1
    if current == 'A':
        i -= 1
        while i >= 0 and path[i][j] != '#':
            if path[i][j] == '.':
                path[i][j] = 'A'
                num += 1
            x = j
            while x < len(path[i]):
                if path[i][x] == 'B':
                    obs += 1
                x += 1
            i -= 1
        current = 'B'
    elif current == 'B':
        j += 1
        while j < len(path[i]) and path[i][j] != '#':
            if path[i][j] == '.':
                path[i][j] = 'B'
                num += 1
            x = i
            while x < len(path):
                if path[x][j] == 'C':
                    obs += 1
                x += 1
            j += 1
        current = 'C'
    elif current == 'C':
        i += 1
        while i < len(path) and path[i][j] != '#':
            if path[i][j] == '.':
                path[i][j] = 'C'
                num += 1
            x = j
            while x >= 0:
                if path[i][x] == 'D':
                    obs += 1
                x -= 1
            i += 1
        current = 'D'
    elif current == 'D':
        j -= 1
        while j >= 0 and path[i][j] != '#':
            if path[i][j] == '.':
                path[i][j] = 'D'
                num += 1
            x = i
            while x >= 0:
                if path[x][j] == 'A':
                    obs += 1
                x -= 1
            j -= 1
        current = 'A'

print(num)
print(obs)