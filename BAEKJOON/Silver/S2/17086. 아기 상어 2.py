from collections import deque

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]


def safe_distance(shark):
    q = deque(shark)
    distance = 0

    while q:
        x, y, cnt = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny, cnt+1])
                else:
                    distance = max(distance, cnt)
    return distance


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
shark = []
max_dist = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j]:
            visited[i][j] = 1
            shark.append([i, j, 0])
print(safe_distance(shark))
