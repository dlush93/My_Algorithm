from collections import deque
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(tomato):
    q = deque(tomato)
    day = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    box[nx][ny] = 1
                    q.append([nx, ny])

    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
            day = max(visited[i][j], day)
    else:
        return day


M, N = map(int, input().split())
box = [list(map(int, input().split())) for i in range(N)]
ripe_tomato = []
visited = [[-1]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripe_tomato.append([i,j])
            visited[i][j] = 0
print(bfs(ripe_tomato))