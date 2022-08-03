N, M = map(int, input().split())
A_arr = list(map(int, input().split())) + [10**10]
B_arr = list(map(int, input().split())) + [10**10]
A_pointer = 0
B_pointer = 0
new_arr = []
while A_pointer+B_pointer < N + M:
    if A_arr[A_pointer] < B_arr[B_pointer]:
        new_arr.append(A_arr[A_pointer])
        A_pointer += 1
    else:
        new_arr.append(B_arr[B_pointer])
        B_pointer += 1
print(*new_arr)