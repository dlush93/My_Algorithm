import sys
input = sys.stdin.readline

def backtracking(cnt, idx):
    global dif
    if cnt == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if arr[i] and arr[j]:
                    start += status[i][j]
                if not arr[i] and not arr[j]:
                    link += status[i][j]

        if abs(start-link) < dif:
            dif = abs(start-link)
        return

    for i in range(idx, N):
        if arr[i]:
            continue
        else:
            arr[i] = 1
            backtracking(cnt+1, i+1)
            arr[i] = 0


N = int(input())
status = [list(map(int,input().split())) for i in range(N)]
dif = 10000000
arr = [0]*N
backtracking(0, 0)
print(dif)