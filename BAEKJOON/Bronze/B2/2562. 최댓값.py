data = [int(input()) for i in range(9)]
max_num = 0
index = 0
for idx, d in enumerate(data,1):
    if d > max_num:
        index = idx
        max_num = d
print(max_num)
print(index)