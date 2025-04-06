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
    rule = content.rstrip().split('|')
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
    for index, value in enumerate(line):
        j = index + 1
        while j < len(line):
            if (value in rulesMap and line[j] in rulesMap[value]) or (line[j] in rulesMap and value not in rulesMap[line[j]]):
                j += 1
            else:
                return False
    return True

valid = []
mid = 0

for line in pages:
    if check(line):
        valid.append(line)
        mid += int(line[len(line) // 2])

print(valid)
print(mid)