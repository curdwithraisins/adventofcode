import re

file = open("./data/input.txt", "r")
content = file.read()
file.close()

diff = 0

res = content.split("do()")

for part in res:
    use = part.split("don't()")
    muls = re.findall("mul\\([0-9]+,[0-9]+\\)", use[0])
    for mul in muls:
        numbers = list(map(int,re.findall("[0-9]+", mul)))
        diff += numbers[0] * numbers[1]

print(diff)