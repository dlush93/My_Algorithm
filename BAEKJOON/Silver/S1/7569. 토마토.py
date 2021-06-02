from collections import deque
dx, dy, dz = [0, 1, 0, -1, 0, 0], [1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, -1]


def bfs(tomato):
    q = deque(tomato)
    day = 0
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if box[nz][nx][ny] == 0 and visited[nz][nx][ny] == -1:
                    box[nz][nx][ny] = 1
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    q.append([nz, nx, ny])

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 0:
                    return -1
                day = max(day, visited[h][n][m])

    return day


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]
ripen_tomato = []
visited = [[[-1]*M for _ in range(N)] for _ in range(H)]
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                ripen_tomato.append([h, n, m])
                visited[h][n][m] = 0
print(bfs(ripen_tomato))
