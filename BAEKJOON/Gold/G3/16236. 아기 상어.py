import sys
from collections import deque
sys.setrecursionlimit(100000)


def hunt_fish(time):
    x, y, second = find_fish(shark[0], shark[1], shark[2])
    board[x][y] = 9
    board[shark[0]][shark[1]] = 0
    shark[0], shark[1] = x, y
    shark[3] += 1
    if shark[3] == shark[2]:
        shark[2] += 1
        shark[3] = 0
    if second == 0:
        return time
    else:
        return hunt_fish(time+second)


def find_fish(x, y, size):
    q = deque()
    fish_list = []
    time = 1000000
    q.append([x, y, 0])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[x][y] = 1
    while q:
        x, y, second = q.popleft()
        if second >= time:
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if board[nx][ny] == 0 or board[nx][ny] == size:
                        q.append([nx, ny, second+1])
                    elif board[nx][ny] < size:
                        fish_list.append([nx, ny])
                        time = second+1
    if len(fish_list) == 0:
        return 0, 0, 0
    col, row = N, N
    for f in fish_list:
        if f[0] < col:
            col = f[0]
            row = f[1]
        elif f[0] == col:
            if f[1] < row:
                col = f[0]
                row = f[1]
    return col, row, time


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
fish = dict()
for i in range(N):
    for j in range(N):
        if 0 < board[i][j] < 9:
            if board[i][j] not in fish:
                fish[board[i][j]] = 0
            fish[board[i][j]] += 1
        elif board[i][j] == 9:
            shark = [i, j, 2, 0]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
print(hunt_fish(0))
