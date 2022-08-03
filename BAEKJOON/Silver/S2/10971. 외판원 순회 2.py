def backtracking(cnt, start, now, cost):
    global min_cost
    if cnt == N-1:
        if board[now][start] == 0:
            return
        min_cost = min(min_cost, cost+board[now][start])
        return

    for nxt in range(N):
        if chk[nxt] and board[now][nxt] != 0:
            chk[nxt] = 0
            backtracking(cnt+1, start,  nxt, cost+board[now][nxt])
            chk[nxt] = 1


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
min_cost = 1000000*N
chk = [1 for _ in range(N)]
for i in range(N):
    chk[i] = 0
    backtracking(0, i, i, 0)
    chk[i] = 1
print(min_cost)