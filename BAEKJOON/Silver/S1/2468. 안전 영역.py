def find_safe(h):
    global max_safe
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] < h < board[i][j]:
                dfs([i, j], h)
                cnt += 1
    max_safe = max(max_safe, cnt)
    return cnt


def dfs(start, h):
    stack = [start]
    visited[start[0]][start[1]] = h
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] < h:
                    visited[nx][ny] = h
                    if board[nx][ny] > h:
                        stack.append([nx, ny])


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_safe = 1
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
visited = [[0 for _ in range(N)] for _ in range(N)]
height = 1
while True:
    if find_safe(height) == 0:
        break
    height += 1
print(max_safe)