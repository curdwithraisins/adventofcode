import re

file = open("./data/input.txt", "r")

values = []

while True:
    content = file.readline()
    if not content:
       break
    row = list(content.rstrip())
    values.append(row)

file.close()

vMap = {}
res = set()

for i, row in enumerate(values):
    for j, value in enumerate(row):
        if value == ".":
            continue
        if value not in vMap:
            vMap[value] = []
        vMap[value].append([i,j])

rowSize = len(values[0])
columnSize = len(values)

for key in vMap:
    if len(vMap[key]) < 2:
        continue
    row = vMap[key]
    for i in range(0, len(row) - 1):
        current = row[i]
        for j in range(i + 1, len(row)):
            distant = row[j]
            if current[0] - (distant[0] - current[0]) >= 0:
                if (distant[1] - current[1]) > 0 and current[1] - (distant[1] - current[1]) >= 0:
                    newValueX = current[0] - distant[0] + current[0]
                    newValueY = current[1] - distant[1] + current[1]
                    res.add(str([newValueX, newValueY]))
                elif (current[1] - distant[1]) > 0 and current[1] + (current[1] - distant[1]) < rowSize:
                    newValueX = current[0] - distant[0] + current[0]
                    newValueY = current[1] - distant[1] + current[1]
                    res.add(str([newValueX, newValueY]))
            if distant[0] + (distant[0] - current[0]) <= columnSize - 1:
                if (distant[1] - current[1]) > 0 and distant[1] + (distant[1] - current[1]) < rowSize:
                    newValueX = distant[0] + (distant[0] - current[0])
                    newValueY = distant[1] + (distant[1] - current[1])
                    res.add(str([newValueX, newValueY]))
                elif (current[1] - distant[1]) > 0 and distant[1] - (current[1] - distant[1]) >= 0:
                    newValueX = distant[0] + (distant[0] - current[0])
                    newValueY = distant[1] - (current[1] - distant[1])
                    res.add(str([newValueX, newValueY]))

print(res)
print(len(res))