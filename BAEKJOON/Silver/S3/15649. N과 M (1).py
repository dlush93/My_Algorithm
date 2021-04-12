def backtracking(cnt):
    if cnt == M:
        print(*arr)
        return

    for i in range(1, N+1):
        if chk_list[i]:
            continue

        chk_list[i] = True
        arr.append(i)
        backtracking(cnt+1)
        arr.pop()
        chk_list[i] = False


N, M = map(int, input().split())
chk_list = [False] * (N+1)
arr = []
backtracking(0)