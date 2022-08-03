def backtracking(cnt):
    global max_gap
    if cnt == N:
        result = 0
        for num1, num2 in zip(arr[:-1], arr[1:]):
            result += abs(num1-num2)
        max_gap = max(max_gap, result)
        return

    for i in range(N):
        if chk[i]:
            chk[i] = 0
            arr.append(num[i])
            backtracking(cnt+1)
            arr.pop()
            chk[i] = 1


N = int(input())
num = list(map(int, input().split()))
chk = [1 for _ in range(N)]
arr = []
max_gap = -1000
backtracking(0)
print(max_gap)