from collections import deque
import sys
input = sys.stdin.readline
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x, y, wall = q.popleft()
        if x == N -1 and y == M-1:
            return visited[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if wall == 1:
                    if MAP[nx][ny] == '1':
                        visited[nx][ny] = visited[x][y] + 1
                        wall -= 1
                        q.append([nx,ny, wall])
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny, wall])
                elif MAP[nx][ny] == '0' and visited[nx][ny] < visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny, wall])
    return -1

N, M = map(int, input().split())
MAP = [list(list(input())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
visited[0][0] = 1
print(bfs([0, 0, 1]))