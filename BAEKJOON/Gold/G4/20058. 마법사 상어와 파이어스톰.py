import sys
input = sys.stdin.readline


def firestorm(L):
    for i in range(0, 2**N, 2**L):
        for j in range(0, 2**N, 2**L):
            arr = []
            for k in range(2**L):
                arr.append(board[i+k][j:j+2**L])
            arr = rot(arr)
            for l in range(2**L):
                board[i+l][j:j+2**L] = arr[l]


def rot(arr):
    return [list(elem) for elem in zip(*arr[::-1])]


def ice_melt():
    new_board = [b[:] for b in board]
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for k in range(4):
                x, y = i+dx[k], j+dy[k]
                if 0 <= x < 2**N and 0 <= y < 2**N:
                    if board[x][y] > 0:
                        cnt += 1
            if cnt < 3 and new_board[i][j] > 0:
                new_board[i][j] -= 1
    return new_board


def big_ice(start):
    global ice, area
    stack = [start]
    big_area = 1
    sum_ice = board[start[0]][start[1]]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 2**N and 0 <= ny < 2**N:
                if visited[nx][ny] == 0 and board[nx][ny] > 0:
                    visited[nx][ny] = 1
                    big_area += 1
                    sum_ice += board[nx][ny]
                    stack.append([nx, ny])
    ice += sum_ice
    area = max(area, big_area)


N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
level = list(map(int, input().split()))
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]

for l in level:
    firestorm(l)
    board = ice_melt()

ice, area = 0, 0
for i in range(2**N):
    for j in range(2**N):
        if board[i][j] != 0 and visited[i][j] == 0:
            visited[i][j] = 1
            big_ice([i, j])
print(ice)
print(area)