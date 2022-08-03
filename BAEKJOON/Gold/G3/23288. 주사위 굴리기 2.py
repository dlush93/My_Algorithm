from collections import deque


def roll_dice(start, direc):
    x, y = start
    nx, ny = x + dx[direc], y + dy[direc]
    if 0 <= nx < N and 0 <= ny < M:
        return nx, ny, direc
    else:
        direc = (direc+2)%4
        nx, ny = x + dx[direc], y + dy[direc]
        return nx, ny, direc


def dice_change(direc):
    if direc == 0:
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif direc == 1:
        dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]
    elif direc == 2:
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    else:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]


def point_chk(B, location):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    x, y = location
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] == B:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    q.append([nx, ny])
    point = B*cnt
    return point


def direction_chk(A, B, direc):
    if A > B:
        direc = (direc+1)%4
    elif A < B:
        direc = (direc-1)%4
    return direc


N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dice = [i for i in range(1, 7)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
result = 0
direction = 0
x, y = 0, 0
for i in range(K):
    x, y, direction = roll_dice([x, y], direction)
    dice_change(direction)
    result += point_chk(MAP[x][y], [x, y])
    direction = direction_chk(dice[5], MAP[x][y], direction)
print(result)