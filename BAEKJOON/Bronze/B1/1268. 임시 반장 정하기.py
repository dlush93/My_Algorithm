student = int(input())
table = [list(map(int, input().split())) for i in range(student)]
array = [[] for i in range(student)]
for i in range(student):
    for j in range(5):
        class_num = table[i][j]
        for k in range(student):
            if i == k:
                continue
            else:
                if table[k][j] == class_num:
                    if k not in array[j]:
                        array[j].append(k)
                        print(i, j, k, array)
class_mate = 0
temp = 0

for index, friends in enumerate(array, 1):
    if len(friends) > class_mate:
        temp = index
print(temp)
print(array)