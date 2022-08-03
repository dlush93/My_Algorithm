from collections import deque


def bfs(start):
    start.append(0)
    q = deque()
    q.append(start)
    visited = [[1 for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]] = 0
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] and board[nx][ny] == 'L':
                    visited[nx][ny] = 0
                    q.append([nx, ny, cnt+1])
    else:
        return cnt


N, M = map(int, input().split())
board = [input() for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
max_cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            max_cnt = max(max_cnt, bfs([i, j]))
print(max_cnt)