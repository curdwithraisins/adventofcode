import re

rulesFile = open("./data/rules.txt", "r")
pagesFile = open("./data/pages.txt", "r")

rules = []
pages = []

rulesMap = {}

while True:
    content = rulesFile.readline()
    if not content:
       break
    rule = content.rulesFile().split('|')
    rules.append(list(rule))
    if rule[0] in rulesMap:
        rulesMap[rule[0]].append(rule[1]) 
    else:
        rulesMap[rule[0]] = [rule[1]]

rulesFile.close()

while True:
    content = pagesFile.readline()
    if not content:
       break
    line = content.rstrip().split(',')
    pages.append(list(line))
    
pagesFile.close()

def check(line):
    index = 0
    while index < len(line):
        j = index + 1
        while j < len(line):
            if (line[index] in rulesMap and line[j] in rulesMap[line[index]]) or (line[j] in rulesMap and line[index] not in rulesMap[line[j]]):
                j += 1
            else:
                val = line[j]
                del line[j]
                line.insert(index, val)
                index -= 1
                break
        index += 1
    return True

valid = []
mid = 0

for line in pages:
    if check(line):
        valid.append(line)
        mid += int(line[len(line) // 2])

print(valid)
print(mid)