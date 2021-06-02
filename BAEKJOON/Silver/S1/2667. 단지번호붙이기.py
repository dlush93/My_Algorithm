from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(start):
    cnt = 1
    q = deque()
    q.append(start)

    while q:
        x, y = q.pop()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if MAP[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    q.append([nx, ny])
    apt.append(cnt)

N = int(input())
MAP = [list(map(int, list(input()))) for i in range(N)]
visited = [[0]*N for i in range(N)]
apt = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1 and visited[i][j] == 0:
            bfs([i, j])
print(len(apt))
for i in sorted(apt):
    print(i)