from collections import deque


def make_wall(cnt):
    if cnt == 3:
        spread_virus(virus)
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(cnt+1)
                board[i][j] = 0


def spread_virus(vi):
    global result
    q = deque(vi)
    nb = [b[:] for b in board]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if nb[nx][ny] == 0:
                    nb[nx][ny] = 2
                    q.append((nx, ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if nb[i][j] == 0:
                cnt += 1
    result = max(result, cnt)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
result = 0
make_wall(0)
print(result)