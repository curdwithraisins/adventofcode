import re

file = open("./data/input.txt", "r")
values = []

while True:
    content = file.readline()
    if not content:
       break
    res = list(map(int,content.rstrip().replace(':', '').split(' ')))
    zero = res[0]
    del res[0]
    values.append((zero, res))

file.close()

def check2(v, l, cur):
    current = cur[:]
    current.append(l[0])
    input = l[1:]
    if len(input) > 0:
        cur = []
        for x in current:
            cur.append(x + input[0]) 
            cur.append(x * input[0])
        return check2(v, input, cur)
    return v in cur

checked = 0

for key in values:
    if check2(key[0], key[1], []):
        checked += key[0]

print(checked)