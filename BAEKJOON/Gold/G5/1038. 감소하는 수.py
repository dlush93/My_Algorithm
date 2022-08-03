def backtracking(arr, length):
    global flag
    if len(arr) > 1 and arr[-2] < arr[-1]:
        return
    if len(arr) == length:
        num.append(''.join(map(str, arr)))

    for i in range(10):
        if i not in arr:
            arr.append(i)
            backtracking(arr, length)
            arr.pop()


N = int(input())
num = []
flag = False
for i in range(1, 11):
    backtracking([], i)

if len(num) > N:
    print(int(num[N]))
else:
    print(-1)