from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def change(d, c):
    if c == 'D':
        d = (d+1)%4
    else:
        d = (d-1)%4
    return d


def snake():
    sec = 0
    x, y = 0, 0
    i = 0
    order = direction.popleft()
    body = deque()
    body.append([x,y])
    while True:
        if sec == order[0]:
            i = change(i, order[1])
            if len(direction) != 0:
                order = direction.popleft()
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 2:
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                body.append([nx, ny])
            else:
                board[nx][ny] = 2
                body.append([nx, ny])
                bx, by = body.popleft()
                board[bx][by] = 0
            x, y = nx, ny
            sec += 1
        else:
            sec += 1
            break
    return sec


N = int(input())
apple = int(input())
board = [[0]*N for i in range(N)]
board[0][0] = 2
for i in range(apple):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
direction = deque()
L = int(input())
for i in range(L):
    X, C = input().split()
    direction.append([int(X), C])
print(snake())