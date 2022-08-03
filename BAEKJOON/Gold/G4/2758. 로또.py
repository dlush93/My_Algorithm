def backtracking(cnt, arr):
    global result
    if cnt == n:
        result += 1
        return
    elif arr[-1]*2 > m:
        return

    for j in range(arr[-1]*2, m+1):
        arr.append(j)
        backtracking(cnt+1, arr)
        arr.pop()


for _ in range(int(input())):
    n, m = map(int, input().split())
    result = 0
    for i in range(1, m+1):
        num_arr = [i]
        backtracking(1, num_arr)
    print(result)