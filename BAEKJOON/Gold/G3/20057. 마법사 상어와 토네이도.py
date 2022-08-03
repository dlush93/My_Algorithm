def tornado():
    x, y = N//2, N//2
    length = 1
    d = 0
    result = 0
    while True:
        for _ in range(2):
            for _ in range(length):
                x, y = x+dx[d], y+dy[d]
                if board[x][y] != 0:
                    result += sand_spread(x, y, d)
                if (x, y) == (0, 0):
                    return result
            else:
                d = (d+1)%4
        else:
            length += 1


def sand_spread(x, y, direc):
    whole_sand = board[x][y]
    sand = 0
    for r in ratio[direc]:
        nx, ny = x+r[0], y+r[1]
        if 0 <= nx < N and 0 <= ny < N:
            whole_sand -= int(board[x][y]*r[2]/100)
            board[nx][ny] += int(board[x][y]*r[2]/100)
        else:
            whole_sand -= int(board[x][y]*r[2]/100)
            sand += int(board[x][y]*r[2]/100)
    board[x][y] = 0
    if 0 <= x+dx[direc] < N and 0 <= y+dy[direc] < N:
        board[x+dx[direc]][y+dy[direc]] += whole_sand
    else:
        sand += whole_sand
    return sand


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
ratio = {0:[[-2, 0, 2], [-1, -1, 10], [-1, 0, 7], [-1, 1, 1], [0, -2, 5],
            [2, 0, 2], [1, -1, 10], [1, 0, 7], [1, 1, 1]],
         1: [[0, -2, 2], [-1, -1, 1], [0, -1, 7], [1, -1, 10], [2, 0, 5],
             [0, 2, 2], [-1, 1, 1], [0, 1, 7], [1, 1, 10]],
         2: [[-2, 0, 2], [-1, -1, 1], [-1, 0, 7], [-1, 1, 10], [0, 2, 5],
             [2, 0, 2], [1, -1, 1], [1, 0, 7], [1, 1, 10]],
         3: [[0, -2, 2], [-1, -1, 10], [0, -1, 7], [1, -1, 1], [-2, 0, 5],
             [0, 2, 2], [-1, 1, 10], [0, 1, 7], [1, 1, 1]]
         }
print(tornado())