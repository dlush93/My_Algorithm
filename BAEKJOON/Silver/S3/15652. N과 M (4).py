def backtracking(arr, cnt):
    if cnt > 1:
        if arr[-2] > arr[-1]:
            return
    if cnt == M:
        print(*arr)
        return

    for i in range(1, N+1):
        arr.append(i)
        backtracking(arr, cnt+1)
        arr.pop()


N, M = map(int, input().split())
backtracking([], 0)