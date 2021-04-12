from collections import deque

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and data[ny][nx] == 1:
                data[ny][nx] = 0
                q.append([ny,nx])

for t in range(int(input())):
    M, N, K = map(int, input().split())
    data = [[0]*M for i in range(N)]
    result = 0
    for i in range(K):
        x, y = map(int, input().split())
        data[y][x] = 1
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                data[i][j] = 0
                bfs([i,j])
                result += 1
    print(result)