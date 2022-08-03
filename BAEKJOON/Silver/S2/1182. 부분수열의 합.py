def backtracking(arr, n):
    global cnt
    if n == N:
        if sum(arr) == S and len(arr) != 0:
            cnt += 1
        return

    arr.append(num[n])
    backtracking(arr, n+1)
    arr.pop()
    backtracking(arr, n+1)


N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
backtracking([], 0)
print(cnt)