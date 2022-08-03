def put_blue(t, x):
    if t == 1:
        for i in range(6):
            if blue_board[x][i] == 1:
                blue_board[x][i-1] = 1
                break
    if t == 2:
        for i in range(5):
            if blue_board[x][i+1] == 1:
                blue_board[x][i] = 1
                blue_board[x][i-1] = 1
                break
        else:
            blue_board[x][-1] = 1
            blue_board[x][-2] = 1
    if t == 3:
        for i in range(6):
            if blue_board[x][i] == 1 or blue_board[x+1][i] == 1:
                blue_board[x][i-1] = 1
                blue_board[x+1][i-1] = 1
                break
    return


def put_green(t, y):
    if t == 1:
        for i in range(6):
            if green_board[i][y] == 1:
                green_board[i-1][y] = 1
                break
    if t == 2:
        for i in range(6):
            if green_board[i][y] == 1 or green_board[i][y+1] == 1:
                green_board[i-1][y] = 1
                green_board[i-1][y+1] = 1
                break
    if t == 3:
        for i in range(5):
            if green_board[i+1][y] == 1:
                green_board[i][y] = 1
                green_board[i-1][y] = 1
                break
        else:
            green_board[-1][y] = 1
            green_board[-2][y] = 1
    return


def remove_block(board):
    point = 0
    if len(board[0]) == 6:
        for j in range(len(board[0])-1, -1, -1):
            for i in range(len(board)):
                if board[i][j] == 0:
                    break
            else:


def chk_board():
    pass


blue_board = [[0 for _ in range(6)] for _ in range(4)]
green_board = [[0 for _ in range(4)] for _ in range(6)]
for _ in range(int(input())):
    t, x, y = map(int, input().split())
    put_blue(t, x)
    put_green(t, y)