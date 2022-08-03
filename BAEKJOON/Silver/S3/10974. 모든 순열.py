def backtracking(arr):
    if len(arr) == N:
        print(*arr)
        return

    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            backtracking(arr)
            arr.pop()

N = int(input())
backtracking([])