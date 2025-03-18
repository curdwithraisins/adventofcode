file = open("./data/input.txt", "r")

list1 = []
list2 = []
diff = 0

while True:
    content = file.readline()
    if not content:
       break
    numbers = content.rstrip().split('   ')
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))

file.close()

list1.sort()
list2.sort()

for index, value in enumerate(list1):
    diff += abs(value - list2[index])

print(diff)