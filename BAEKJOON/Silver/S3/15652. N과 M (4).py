def backtracking(cnt):
    if len(arr) > 1:
        if arr[-1] < arr[-2]:
            return
    if cnt == M:
        print(*arr)
        return

    for i in range(1, N+1):
        arr.append(i)
        backtracking(cnt+1)
        arr.pop()


N, M = map(int, input().split())
arr = []
backtracking(0)
