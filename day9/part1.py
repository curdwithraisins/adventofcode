import re

file = open("./data/input.txt", "r")

res = ""

while True:
    content = file.readline()
    if not content:
       break
    res = list(content.rstrip())

file.close()

newStr = []
current = 0
isDot = False

for x in res:
    for v in range(0, int(x)):
        k = '.' if isDot else current
        newStr.append(k)
    current = current + 1 if isDot else current
    isDot = not isDot

front = 0
back = len(newStr) - 1

while front < back:
    if newStr[front] == '.' and newStr[back] != '.':
        newStr[front] = newStr[back]
        newStr[back] = '.'
        back -= 1
        while newStr[back] == '.':
            back -= 1
    front += 1

i = 0
calc = 0
while newStr[i] != '.':
    calc += newStr[i] * i
    i += 1

print(calc)