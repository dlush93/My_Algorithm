import sys
input = sys.stdin.readline


def hunt_shark(col):
    for row in range(R):
        if board[row][col] != 0:
            size = shark[board[row][col]][4]
            del shark[board[row][col]]
            board[row][col] = 0
            return size
    return 0


def move_shark():
    new_board = [[0 for _ in range(C)] for _ in range(R)]
    for shk in range(1, M+1):
        if shk not in shark:
            continue
        x, y, s, d, z = shark[shk]
        ns = s
        direc = 1
        while ns > 0:
            nx, ny = x+dx[d-1]*direc, y+dy[d-1]*direc
            if 0 <= nx < R and 0 <= ny < C:
                x, y = nx, ny
                ns -= 1
            else:
                direc *= -1
        if direc == -1:
            if d%2:
                d += 1
            else:
                d -= 1
        if new_board[x][y] == 0:
            new_board[x][y] = shk
            shark[shk] = [x, y, s, d, z]
        else:
            if shark[new_board[x][y]][4] > shark[shk][4]:
                del shark[shk]
            else:
                del shark[new_board[x][y]]
                new_board[x][y] = shk
                shark[shk] = [x, y, s, d, z]
    return new_board


R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
shark = dict()
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    shark[i] = [r-1, c-1, s, d, z]
    board[r-1][c-1] = i
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
result = 0

for c in range(C):
    result += hunt_shark(c)
    board = move_shark()
print(result)