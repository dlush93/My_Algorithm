def road_chk():
    cnt = 0
    for i in range(N):
        for j in range(2):
            if bridge_chk(i, j):
                cnt += 1
    return cnt


def bridge_chk(line, direc):
    start, end, tilt = 0, 0, 0
    if direc == 0:
        while end < N:
            if abs(board[line][end] - board[line][start]) > 1:
                return False

            elif board[line][end] - board[line][start] == 1:
                if tilt == 0:
                    tilt = 1
                if tilt < 0:
                    return False
                else:
                    if end - start >= L:
                        start = end + 1
                        tilt = 0

            elif board[line][end] - board[line][start] == -1:
                if tilt == 0:
                    tilt -= 1
                if tilt == 1:
                    return False
                else:
                    if tilt*-1 >= L:
                        start = end + 1
                        tilt = 0
            end += 1
    else:
        while end < N:
            if abs(board[end][line] - board[start][line]) > 1:
                return False

            elif board[end][line] - board[start][line] == 1:
                if tilt == 0:
                    tilt = 1
                if tilt < 0:
                    return False
                else:
                    if end - start >= L:
                        start = end + 1
                        tilt = 0

            elif board[end][line] - board[start][line] == -1:
                if tilt == 0:
                    tilt -= 1
                if tilt == 1:
                    return False
                else:
                    if tilt * -1 >= L:
                        start = end + 1
                        tilt = 0
            end += 1

    if tilt != 0 and end - start < L:
        return False
    print(line, direc)
    return True


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(road_chk())