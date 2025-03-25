import re

file = open("./data/input.txt", "r")
content = file.read()
file.close()

diff = 0

res = re.findall("mul\\([0-9]+,[0-9]+\\)", content)

for mul in res:
    numbers = list(map(int,re.findall("[0-9]+", mul)))
    diff += numbers[0] * numbers[1]

print(diff)