from collections import deque
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            return cnt[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '1' and visited[nx][ny]:
                    visited[nx][ny] = False
                    cnt[nx][ny] = cnt[x][y] + 1
                    q.append([nx,ny])

N, M = map(int, input().split())
arr = [list(input()) for i in range(N)]
cnt = [[0]*M for i in range(N)]
cnt[0][0] = 1
visited = [[True]*M for i in range(N)]
visited[0][0] = False
print(bfs([0,0]))