student = int(input())
student_list = dict()
table = [list(map(int, input().split())) for i in range(student)]

for s in range(student):
    if s not in student_list:
        student_list[s] = set()
    for i in range(5):
        class_num = table[s][i]
        for j in range(student):
            if class_num == table[j][i]:
                student_list[s].add(j)
max_friend = 0
result = 0
for key, value in student_list.items():
    if len(value) > max_friend:
        result = key + 1
        max_friend = len(value)
print(result)
