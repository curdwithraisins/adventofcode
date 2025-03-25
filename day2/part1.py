file = open("./data/input.txt", "r")

list1 = []
diff = 0

def inc(list) -> int:
    for i in range(0, len(list) - 1):
        if not 0 < list[i+1] - list[i] < 4:
            return 0
    return 1

def dec(list) -> int:
    for i in range(0, len(list) - 1):
        if not 0 < list[i] - list[i+1] < 4:
            return 0
    return 1

while True:
    content = file.readline()
    if not content:
       break
    numbers = list(map(int, content.rstrip().split(' ')))
    diff += inc(numbers) if (numbers[0] < numbers[1]) else dec(numbers) 

file.close()

print(diff)