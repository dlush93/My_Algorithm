import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1, -1], [0, 1, 1, 1, 0, -1, -1, -1]


def wave():
    q = deque()
    cnt = 0
    broken = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if castle[i][j] == '.':
                q.append((i, j))
            else:
                castle[i][j] = int(castle[i][j])

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if castle[nx][ny] != '.':
                    castle[nx][ny] -= 1
                if castle[nx][ny] == 0:
                    broken[nx][ny] = broken[x][y] + 1
                    q.append((nx, ny))
                    cnt = max(cnt, broken[nx][ny])
    return cnt


H, W = map(int, input().split())
castle = [list(input()) for _ in range(H)]
print(wave())