file = open("./data/input.txt", "r")

list1 = []
list2 = {}
diff = 0

while True:
    content = file.readline()
    if not content:
       break
    numbers = content.rstrip().split('   ')
    list1.append(int(numbers[0]))
    if int(numbers[1]) in list2:
        list2[int(numbers[1])] += 1
    else:
        list2[int(numbers[1])] = 1

file.close()

for value in list1:
    coef = list2[value] if value in list2 else 0
    diff += value * coef

print(diff)