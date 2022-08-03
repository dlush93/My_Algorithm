def backtracking(cnt):
    if cnt == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if i not in num_set:
            num_set.add(i)
            arr.append(i)
            backtracking(cnt+1)
            arr.pop()
            num_set.discard(i)


N, M = map(int, input().split())
num_set = set()
arr = []
backtracking(0)