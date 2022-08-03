from collections import deque
from itertools import combinations


def spread_virus(arr):
    q = deque(arr)
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    for a in arr:
        visited[a[0]][a[1]] = 0
    while q:
        x, y, t, save = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    if board[nx][ny] == 0:
                        visited[nx][ny] = t+1+save
                        q.append([nx, ny, t+1+save, 0])
                    elif board[nx][ny] == 2:
                        visited[nx][ny] = t
                        q.append([nx, ny, t, save+1])
    time = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and board[i][j] == 0:
                return N*N
            if visited[i][j] != 0:
                time = max(time, visited[i][j])
    return time


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = [[i, j, 0, 0] for i in range(N) for j in range(N) if board[i][j] == 2]
result = N*N
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for comb in combinations(virus, M):
    result = min(result, spread_virus(comb))
if result == N*N:
    print(-1)
else:
    print(result)