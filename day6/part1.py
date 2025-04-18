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
        break
    if '>' in path[i]:
        j = path[i].index('>')
        break
    if '<' in path[i]:
        j = path[i].index('<')
        break
    if 'v' in path[i]:
        j = path[i].index('v')
        break
    i += 1

num = 1
current = path[i][j]

while i >= 0 and i < len(path) and j >= 0 and j < len(path[i]):
    print(path)
    print(current)
    print(i,j)
    if path[i][j] == '#':
        if current == '^':
            j += 1
        elif current == '>':
            i += 1
        elif current == 'v':
            j -= 1
        elif current == '<':
            i -= 1
    if current == '^':
        i -= 1
        while i > 0 and path[i][j] != '#':
            if path[i][j] == '.':
                path[i][j] = 'X'
                num += 1
            i -= 1
        current = '>'
    elif current == '>':
        j += 1
        while j < len(path[i]) and path[i][j] != '#':
            if path[i][j] == '.':
                path[i][j] = 'X'
                num += 1
            j += 1
        current = 'v'
    elif current == 'v':
        i += 1
        while i < len(path) and path[i][j] != '#':
            if path[i][j] == '.':
                path[i][j] = 'X'
                num += 1
            i += 1
        current = '<'
    elif current == '<':
        j -= 1
        while j > 0 and path[i][j] != '#':
            if path[i][j] == '.':
                path[i][j] = 'X'
                num += 1
            j -= 1
        current = '^'

print(num)