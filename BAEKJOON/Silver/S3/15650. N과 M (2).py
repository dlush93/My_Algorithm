def backtracking(cnt):
    if cnt > 1:
        if arr[-2] > arr[-1]:
            return
    if cnt == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if num[i]:
            num[i] = 0
            arr.append(i)
            backtracking(cnt+1)
            arr.pop()
            num[i] = 1


N, M = map(int, input().split())
arr = []
num = [1 for _ in range(N+1)]
backtracking(0)