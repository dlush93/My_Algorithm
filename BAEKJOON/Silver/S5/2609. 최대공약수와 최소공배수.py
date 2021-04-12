A, B = map(int, input().split())
temp_A = max(A,B)
temp_B = min(A,B)
min_num = 0
max_num = 0
flag = True
while flag:
    if temp_A%temp_B == 0:
        min_num = temp_B
        flag = False
    else:
        temp_A, temp_B = temp_B, temp_A%temp_B
max_num = A*B//min_num
print(min_num)
print(max_num)