file = open("input.txt", "r")

list1 = []
diff = 0

def inc_def(list) -> int:
    for i in range(0, len(list) - 1):
        if not 0 < list[i+1] - list[i] < 4:
            return 0
    return 1

def dec_def(list) -> int:
    for i in range(0, len(list) - 1):
        if not 0 < list[i] - list[i+1] < 4:
            return 0
    return 1

def inc(list) -> int:
    removed = False
    i = 0

    while i < len(list) - 1:
        if not 0 < list[i+1] - list[i] < 4:
            if not removed:
                list_c1 = list.copy()
                del list_c1[i]
                list_c2 = list.copy()
                del list_c2[i+1]
                val1 = inc_def(list_c1) if (list_c1[0] < list_c1[1]) else dec_def(list_c1) 
                val2 = inc_def(list_c2) if (list_c2[0] < list_c2[1]) else dec_def(list_c2)
                return val1 or val2
            else:
                print("INC: " + ', '.join(map(str, list)))
                return 0
        i += 1
    return 1

def dec(list) -> int:
    removed = False
    i = 0

    while i < len(list) - 1:
        if not 0 < list[i] - list[i+1] < 4:
            if not removed:
                list_c1 = list.copy()
                del list_c1[i]
                list_c2 = list.copy()
                del list_c2[i+1]
                val1 = inc_def(list_c1) if (list_c1[0] < list_c1[1]) else dec_def(list_c1) 
                val2 = inc_def(list_c2) if (list_c2[0] < list_c2[1]) else dec_def(list_c2)
                return val1 or val2
            else:
                print("DEC: " + ', '.join(map(str, list)))
                return 0
        i += 1
    return 1

while True:
    content = file.readline()
    if not content:
       break
    numbers = list(map(int, content.rstrip().split(' ')))
    val = inc(numbers) if (numbers[0] < numbers[1]) else dec(numbers) 
    if val == 0:
        numbers.remove(numbers[0])
        val = inc_def(numbers) if (numbers[0] < numbers[1]) else dec_def(numbers)
    diff += val

file.close()

print(diff)